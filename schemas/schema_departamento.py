from pydantic import BaseModel
from datetime import datetime

class DepartamentoCreate(BaseModel):
    nombre: str
    descripcion: str
    ubicacion: str
    estado: str

class DepartamentoRead(BaseModel):
    nombre: str
    descripcion: str
    ubicacion: str
    estado: str  


class DepartamentoUpdatePartial(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    ubicacion: str | None = None
    estado: str | None = None


class DepartamentoDelete(BaseModel):
    is_active: bool