from __future__ import annotations
from typing import Any

from pydantic import BaseModel


class ProductParams(BaseModel):
    idProducto: int
    precio: int


class UserParams(BaseModel):
    userId: int
    country: str
    extra: dict[str, Any]
    detailDescription: str
    paymentKind: str


class BuscadorModel(BaseModel):
    idVenta: int
    dispatchId: int
    idUsuario: int
    productParams: ProductParams
    userParams: UserParams
