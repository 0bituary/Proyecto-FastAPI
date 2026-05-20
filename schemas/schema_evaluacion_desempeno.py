from pydantic import BaseModel
from datetime import datetime

class EvaluacionCreate(BaseModel):
    fecha: datetime
    periodo: str
    observaciones: str
    calificacion_general: str  

class EvaluacionRead(BaseModel):
    fecha: datetime
    periodo: str
    observaciones: str
    calificacion_general: str  


class EvaluacionUpdatePartial(BaseModel):
    fecha: datetime | None = None
    periodo: str | None = None
    observaciones: str | None = None
    calificacion_general: str | None = None


class EvaluacionDelete(BaseModel):
    is_active: bool