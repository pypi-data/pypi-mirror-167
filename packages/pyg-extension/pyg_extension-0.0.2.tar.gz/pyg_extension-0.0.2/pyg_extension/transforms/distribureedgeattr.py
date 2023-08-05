import math

import torch
from torch_cluster import radius_graph
from torch_geometric.transforms import BaseTransform
from torch_geometric.utils import remove_self_loops


class AddEdge(BaseTransform):
    """Add edge index, with no pbc."""

    def __init__(self, cutoff=5.0, ):
        self.cutoff = cutoff

    def __call__(self, data):
        edge_index = radius_graph(data.pos, r=self.cutoff, batch=data.batch)
        edge_index, _ = remove_self_loops(edge_index)
        row, col = edge_index[0], edge_index[1]
        edge_weight = (data.pos[row] - data.pos[col]).norm(dim=-1)

        data.edge_index = edge_index
        data.edge_weight = edge_weight
        data.edge_attr = edge_weight.reshape(-1, 1)
        return data


class AddAttrToWeight(BaseTransform):
    """Add edge index, with no pbc."""

    def __call__(self, data):
        if not hasattr(data, "edge_weight") or data.edge_weight is None:
            data.edge_weight = torch.linalg.norm(data.edge_attr, dim=1)
        return data


class AddAttrSumToAttrAndWeight(BaseTransform):
    """Add edge index, with no pbc."""

    def __call__(self, data):
        if not hasattr(data, "edge_weight") or data.edge_weight is None:
            data.edge_weight = torch.linalg.norm(data.edge_attr, dim=1)
            data.edge_attr = data.edge_weight.reshape(-1, 1)
        return data


class AddAttrSumToAttr(BaseTransform):
    """Add edge index, with no pbc."""

    def __call__(self, data):
        assert hasattr(data, "edge_attr") and data.edge_attr is not None
        assert data.edge_attr.shape[1] == 3
        if not hasattr(data, "edge_weight") or data.edge_weight is None:
            data.edge_weight = torch.linalg.norm(data.edge_attr, dim=1)

        wei = data.edge_weight

        data.edge_attr = torch.cat((wei.reshape(-1, 1), data.edge_attr), dim=1)

        return data


class DistributeEdgeAttr(BaseTransform):
    """Compact with rotnet network (deep potential)"""

    def __init__(self, r_cs=2.0, r_c=6.0, cat_weight_attr=True):
        super().__init__()
        self.r_cs = r_cs
        self.r_c = r_c
        self.cat_weight_attr = cat_weight_attr

    def __call__(self, data):
        assert hasattr(data, "edge_attr") and data.edge_attr is not None
        assert data.edge_attr.shape[1] == 3
        if not hasattr(data, "edge_weight") or data.edge_weight is None:
            data.edge_weight = torch.linalg.norm(data.edge_attr, dim=1)

        wei = data.edge_weight

        attr = torch.cat((wei.reshape(-1, 1), data.edge_attr), dim=1)

        r_cs = self.r_cs
        r_c = self.r_c

        sr = torch.clone(attr[:, 0])
        r_m1 = sr <= r_cs
        r_m3 = sr >= r_c
        r_m2 = ~(r_m3 | r_m1)

        sr[r_m1] = 1 / sr[r_m1]

        u = (sr[r_m2] - r_cs) / (self.r_c - self.r_cs)
        sr[r_m2] = 1 / sr[r_m2] * (0.5 * torch.cos(math.pi * u) + 0.5)  # from deep Potential
        sr[r_m3] = 0

        attr = attr / attr[:, 0].reshape(-1, 1) * sr.reshape(-1, 1)

        data.edge_attr = attr
        data.edge_weight = sr
        return data
