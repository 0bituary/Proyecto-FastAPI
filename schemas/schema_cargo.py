from pydantic import BaseModel
from decimal import Decimal

class CargoCreate(BaseModel):
    nombre: str
    salario_base: Decimal
    jerarquia: str
    descripcion: str
    estado: bool

class CargoRead(BaseModel):
    nombre: str
    salario_base: Decimal
    jerarquia: str
    descripcion: str
    estado: bool

class CargoUpdatePartial(BaseModel):
    nombre: str | None = None
    salario base: Decimal | None = None
    jerarquia: str | None = None
    descripcion: str | None = None
    estado: bool | None = None


class CargoDelete(BaseModel):
    is_active: bool