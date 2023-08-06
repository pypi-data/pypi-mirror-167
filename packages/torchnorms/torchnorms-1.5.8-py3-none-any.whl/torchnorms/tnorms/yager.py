# -*- coding: utf-8 -*-

import torch
from torch import nn, Tensor
from torch import isnan,tensor
from torch import sum as summer
from torchnorms.tnorms.base import BaseTNorm

from typing import Optional


class YagerTNorm(BaseTNorm):
    def __init__(self,
                 p: Optional[Tensor] = None,
                 default_p: float = 2.0) -> None:
        super().__init__()
        self.p = p
        if self.p is None:
            self.p = nn.Parameter(torch.tensor(default_p))
        assert len(self.p.shape) == 0

        self.relu = torch.nn.ReLU()
        self.eps = 0.01

    def __call__(self,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        res: Optional[Tensor] = None

        self.adjust_nan_param()

        self.p.data = self.relu(self.p.data)
        if self.p == 0:
            self.p.data += self.eps

        p_1 = torch.pow(1.0 - a, self.p)
        p_2 = torch.pow(1.0 - b, self.p)
        p_3 = torch.pow(p_1 + p_2, 1.0 / self.p)
        res = torch.minimum(torch.tensor(1.0) , p_3)
        res = 1.0 - res

        return res

    def adjust_nan_param(self):
        for param in self.parameters():
            if summer(isnan(param)):
                param.data = tensor(0.1, device = param.device)
