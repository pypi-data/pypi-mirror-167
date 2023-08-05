import os
import os.path as osp

import torch
import torch_geometric.transforms as T
from torch_geometric.data import Data
from torch_geometric.loader import DataLoader
from torch_geometric.utils import remove_self_loops

from pyg_extension.data.dataset import InMemoryDatasetGeo
from pyg_extension.nn.flow_geo import LearningFlow
from pyg_extension.nn.schnetuser import SchNetUser

target = 0
dim = 64

class QM9User(InMemoryDatasetGeo):

    @property
    def processed_file_names(self):
        return ['data_v3.pt']

    def process(self):
        data_list = torch.load(self.raw_paths[0])
        data_list = [Data(**data_dict) for data_dict in data_list] # just for qm9_v3.pt data

        if self.pre_filter is not None:
            data_list = [d for d in data_list if self.pre_filter(d)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(d) for d in data_list]

        self.data, self.slices = self.collate(data_list)

        torch.save((self.data, self.slices), self.processed_paths[0])


class MyTransform(object):
    def __call__(self, data):
        # Specify target.
        data.y = data.y[:, target]
        return data


class Complete(object):
    def __call__(self, data):
        device = data.edge_index.device

        row = torch.arange(data.num_nodes, dtype=torch.long, device=device)
        col = torch.arange(data.num_nodes, dtype=torch.long, device=device)

        row = row.view(-1, 1).repeat(1, data.num_nodes).view(-1)
        col = col.repeat(data.num_nodes)
        edge_index = torch.stack([row, col], dim=0)

        edge_attr = None
        if data.edge_attr is not None:
            idx = data.edge_index[0] * data.num_nodes + data.edge_index[1]
            size = list(data.edge_attr.size())
            size[0] = data.num_nodes * data.num_nodes
            edge_attr = data.edge_attr.new_zeros(size)
            edge_attr[idx] = data.edge_attr

        edge_weight = (data.pos[row] - data.pos[col]).norm(dim=-1)

        edge_index1, edge_attr = remove_self_loops(edge_index, edge_attr)
        edge_index1, edge_weight = remove_self_loops(edge_index, edge_weight)
        data.edge_attr = edge_attr
        data.edge_weight = edge_weight
        data.edge_index = edge_index1

        data.state_attr = torch.zeros((1, 2))

        return data


path = osp.join(osp.dirname(osp.realpath(__file__)), 'qm9_v3')
transform = T.Compose([MyTransform(), Complete()])
dataset = QM9User(path, pre_transform=transform, re_process_init=False).shuffle()

# Normalize targets to mean = 0 and std = 1.

mean = dataset.data.y.mean()
std = dataset.data.y.std()
dataset.data.y = (dataset.data.y - mean) / std


# # Split datasets.
test_dataset = dataset[:1000]
val_dataset = dataset[1000:2000]
train_dataset = dataset[2000:3000]
test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)
val_loader = DataLoader(val_dataset, batch_size=128, shuffle=False)
train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
#
device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
# # model = CGGRUNet(11, 5, cutoff=5.0).to(device)
# # model = CrystalGraphConvNet(11, 5, cutoff=5.0).to(device)
# # model = CrystalGraphGCN(11, 5, cutoff=5.0).to(device)
# # model = CrystalGraphGCN2(11, 5, cutoff=5.0).to(device)
# # model = SchNet(0,0,simple_edge=True).to(device)
# # model = MEGNet(11, 5, cutoff=5.0,num_state_features=2).to(device)
# # model = SchNet(11,5,simple_edge=False).to(device)
model = SchNetUser(nc_node_hidden= 64, num_filters= 64,
                 num_interactions= 4, nc_edge_hidden= 50,
                 cutoff= 7.0, max_num_neighbors= 32).to(device)
# # model = SchNet(11,5,simple_edge=False,simple_z=False).to(device)
# # model = CrystalGraphConvNet(0,5,simple_edge=False,simple_z=True).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=5e-4)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min',
                                                       min_lr=5e-4)

lf = LearningFlow(model, train_loader, validate_loader=val_loader, device="cuda:0",
                  optimizer=None, clf=False, loss_method=None, milestones=None,
                  weight_decay=0.0, checkpoint=True, scheduler=scheduler,
                  loss_threshold=0.1, print_freq=None, print_what="all")
lf.run(500)

