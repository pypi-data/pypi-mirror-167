# -*- coding: utf-8 -*-

import torch
from torch import Tensor, nn
from torchnorms.negations.base import BaseNegation


class StandardNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'standard'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        return 1.0 - a


class AffineNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'affine'
        # 1 - score(s, p, o)
        self.affine_scale = nn.Parameter(torch.tensor(- 1.0), requires_grad=True)
        self.affine_translate = nn.Parameter(torch.tensor(+ 1.0), requires_grad=True)

    def __call__(self,
                 a: Tensor) -> Tensor:
        # return torch.sigmoid(a*self.afffine_scale + self.affine_translate)
        return (a * self.affine_scale) + self.affine_translate


class StrictNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'strict'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        return 1.0 - torch.pow(a, 2)


class StrictCosNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'strict_cosine'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        pi = torch.acos(torch.zeros(1)).item() * 2
        res = 0.5 * (1 + torch.cos(pi * a))
        return res
