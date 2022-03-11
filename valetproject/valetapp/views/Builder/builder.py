from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_valet_service_a(self) -> None:
        pass

    @abstractmethod
    def add_valet_service_b(self) -> None:
        pass

    @abstractmethod
    def add_valet_service_c(self) -> None:
        pass