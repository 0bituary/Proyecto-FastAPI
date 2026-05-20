from pydantic import BaseModel
from datetime import datetime

class NominaCreate(BaseModel):
    periodo_pago: datetime
    salario_base: Decimal
    deducciones: Decimal
    bonificaciones: Decimal
    neto_pagar: Decimal

class NominaRead(BaseModel):
    periodo_pago: datetime
    salario_base: Decimal
    deducciones: Decimal
    bonificaciones: Decimal
    neto_pagar: Decimal


class NominaUpdatePartial(BaseModel):
    periodo_pago: datetime | None = None
    salario_base: Decimal | None = None
    deducciones: Decimal | None = None
    bonificaciones: Decimal | None = None
    neto_pagar: Decimal | None = None
    estado: str | None = None


class NominaDelete(BaseModel):
    is_active: bool