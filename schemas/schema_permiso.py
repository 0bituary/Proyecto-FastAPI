from pydantic import BaseModel
from datetime import datetime

class PermisoCreate(BaseModel):
    solicitud: str
    motivo: str
    fecha_solicitud: datetime
    estado: str

class PermisoRead(BaseModel):
    solicitud: str
    motivo: str
    fecha_solicitud: datetime
    estado: str 


class PermisoUpdatePartial(BaseModel):
    solicitud: str | None = None
    motivo: str | None = None
    fecha_solicitud: datetime | None = None
    estado: str | None = None


class PermisoDelete(BaseModel):
    is_active: bool