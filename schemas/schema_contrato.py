from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class ContratoCreate(BaseModel):
    tipo_contrato: str
    fecha_inicio: datetime
    fecha_fin: datetime
    salario: Decimal
    condiciones_generales: str


class ContratoEmpleadoRead(BaseModel):
    tipo_contrato: str
    fecha_inicio: datetime
    fecha_fin: datetime
    salario: Decimal
    condiciones_generales: str


class ContratoUpdatePartial(BaseModel):
    tipo_contrato: str | None = None
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None
    salario: str | None = None
    condiciones_generales: str | None = None
    


class ContratoDelete(BaseModel):
    is_active: bool