from pydantic import BaseModel
from datetime import datetime

class EmpleadoCreate(BaseModel):
    documento: str
    nombre: str
    correo: str
    telefono: int
    fecha_ingreso: datetime
    estado: str

class EmpleadoRead(BaseModel):
    documento: str
    nombre: str
    correo: str
    telefono: int
    fecha_ingreso: datetime
    estado: str    


class EmpleadoUpdatePartial(BaseModel):
    documento: str | None = None
    nombre: str | None = None
    correo: str | None = None
    telefono: int | None = None
    fecha_ingreso: datetime | None = None
    estado: str | None = None


class EmpleadoDelete(BaseModel):
    is_active: bool