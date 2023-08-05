import torch
import torch.nn as nn
from torch import Tensor
from torch_geometric.nn import Set2Set

from pyg_extension.nn.basemodel import BaseCrystalModel
from pyg_extension.nn.mgelayer import MegnetModule


class MEGNetUser(BaseCrystalModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nc_edge_hidden, self.nc_node_hidden, self.nc_state_hidden = 100, 16, 2

        self.layer_emb_node = nn.Embedding(self.nnvocal, self.nc_node_hidden)
        self.m1 = MegnetModule(self.nc_edge_hidden, self.nc_node_hidden, self.nc_state_hidden, prep=True)
        self.m2 = MegnetModule(32, 32, 32, prep=False)
        self.m3 = MegnetModule(32, 32, 32, prep=False)
        self.se = Set2Set(32, 1)
        self.sv = Set2Set(32, 1)
        self.hiddens = nn.Sequential(
            nn.Linear(160, 32),
            nn.Softplus(),
            nn.Linear(32, 16),
            nn.Softplus(),
            nn.Linear(16, 1)
        )

    def _forward(self, x, data):
        """This function can be re-write."""

        batch = data.batch
        edge_index = data.edge_index if data.edge_index is not None else data.adj_t
        edge_attr = data.edge_attr
        state_attr = data.state_attr

        if isinstance(edge_index, Tensor):
            index = edge_index[0]
        else:
            index = edge_index.storage.row()

        bond_batch = batch[index]

        x, edge_attr, state_attr = self.m1(x, edge_index, edge_attr, state_attr, batch, bond_batch)
        x, edge_attr, state_attr = self.m2(x, edge_index, edge_attr, state_attr, batch, bond_batch)
        x, edge_attr, state_attr = self.m3(x, edge_index, edge_attr, state_attr, batch, bond_batch)
        x = self.sv(x, batch)
        edge_attr = self.se(edge_attr, bond_batch)
        tmp = torch.cat((x, edge_attr, state_attr), 1)
        out = self.hiddens(tmp)
        return out
