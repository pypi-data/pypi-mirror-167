# -*- coding: utf-8 -*-

import torch
from torch import Tensor

from torchnorms.tnorms.base import BaseTNorm


class MinimumTNorm(BaseTNorm):
    """
    Minimum t-norm, also called the Gödel t-norm
    """
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        return torch.min(a, b)


class ProductTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        return a * b


class LukasiewiczTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        return torch.relu(a + b - 1.0)


class DrasticTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        b_mask = b * (a >= 1.0)
        a_mask = a * (b >= 1.0)
        return torch.max(a_mask, b_mask)


class EinsteinTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        return (a * b) / (1.0 + (1.0 - a) * (1.0 - b))


class BoundedTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        return torch.clip(a + b - 1.0, min=0.0)


class NilpotentMinimumTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def __call__(cls,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        mask = (a + b) > 1.0
        return torch.min(a, b) * mask


class HamacherProductTNorm(BaseTNorm):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        a_nnz = a > 0.0
        b_nnz = b > 0.0
        mask = torch.logical_and(a_nnz, b_nnz)
        res = (a * b) / (a + b - a * b)
        return res * mask


class HamacherSimpleTNorm(BaseTNorm):
    """
    Hamacher t-norm from https://ece.uwaterloo.ca/~dwharder/Maplesque/FuzzySets/t-norm.html
    """
    def __init__(self) -> None:
        super().__init__()

    def __call__(self,
                 a: Tensor,
                 b: Tensor) -> Tensor:
        res = (a * b) / (a + b - a * b)
        return res
