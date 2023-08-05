import unittest

import torch
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
from torch import nn, Tensor
from torch.utils.data import Dataset, DataLoader, TensorDataset

from mgetool.show import BasePlot
from pyg_extension.nn.resnet import ResBlockSameSize, ResBlockDiffSize
from torch.nn import Module, ModuleList, ReLU, Sequential

class Li2(nn.Linear):
    def forward(self, input: Tensor, **kwargs) -> Tensor:
        return super().forward(input)

class ResNet(Module):
    def __init__(self, fea):
        super().__init__()

        self.block1 = ResBlockDiffSize(Li2, layer_size_seq=(fea,16,32, 64), force_x_match=True)
        self.block2 = ResBlockSameSize(Li2,n_res=1, in_features=64, out_features=64, force_x_match=True)
        self.out = Sequential(Li2(64,128),ReLU(), Li2(128,1))

    def forward(self,x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.out(x)
        return x

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from sklearn.datasets import fetch_california_housing
        X, y = fetch_california_housing(return_X_y=True)
        X, y = shuffle(X, y, random_state=0)
        mms = MinMaxScaler()

        X = X[:5000]
        y = y[:5000]
        X = mms.fit_transform(X)
        X = torch.from_numpy(X).float()
        y = torch.from_numpy(y).float().reshape(-1, 1)
        self.fea = X.shape[1]
        self.X =X
        self.y =y

    def test_something(self):
        resn = ResNet(self.fea)
        yb = resn(self.X)
        assert yb.shape==self.y.shape


    def test_flow(self):
        model = ResNet(self.fea)
        me = "cuda:0"
        me = "cpu"
        if me =="cuda:0":
            model.to("cuda:0")
            X = self.X.cuda()
            y = self.y.cuda()
        else:
            X = self.X
            y = self.y
        td = TensorDataset(X, y)

        train_loader = DataLoader(td, batch_size=256)
        optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
        model.train()
        loss_method = torch.nn.L1Loss()
        for epi in range(500):
            lossi=0
            for bx, by in train_loader:
                model.zero_grad()

                y_pred = model(bx)

                lossi = loss_method(y_pred, by)
                lossi.backward()
                optimizer.step()
            print(lossi)
        bp = BasePlot()
        plt = bp.scatter_45_line(by.detach().numpy(), y_pred.detach().numpy(), strx='y_true', stry='y_predict')
        plt.show()
if __name__ == '__main__':
    unittest.main()
