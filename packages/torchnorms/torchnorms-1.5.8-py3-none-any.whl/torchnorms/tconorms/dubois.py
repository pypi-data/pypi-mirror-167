# -*- coding: utf-8 -*-

import torch
from torch import nn, Tensor
from torch import isnan, tensor
from torch import sum as summer
from torchnorms.tconorms.base import BaseTCoNorm

from typing import Optional


class DuboisTCoNorm(BaseTCoNorm):
    def __init__(self,
                 p: Optional[Tensor] = None,
                 default_p: float = 0.1) -> None:
        super().__init__()
        self.p = p
        if self.p is None:
            assert default_p >= -1.0

            self.p = nn.Parameter(torch.tensor(default_p))
        else:
            assert self.p >= -1.0

        assert len(self.p.shape) == 0

    def __call__(self,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        self.adjust_nan_param()

        self.p.data = torch.clamp(self.p.data, min=0, max=1)

        p_1 = a + b
        p_2 = p_1 + (self.p * a * b)
        res = torch.minimum(p_2, torch.tensor(1))

        return res

    def adjust_nan_param(self):
        for param in self.parameters():
            if summer(isnan(param)):
                param.data = tensor(0.1, device=param.device)
