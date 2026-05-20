from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import date



class Departamento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, unique=True)
    descripcion: str
    ubicacion: str
    estado: bool = Field(default=True) # Campo de estado obligatorio [cite: 12]
    
    empleados: List["Empleado"] = Relationship(back_populates="departamento")

class Empleado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    documento: str = Field(index=True, unique=True)
    correo: str
    telefono: int
    fecha_ingreso: date
    estado: str = Field(default="Activo")
    
    departamento_id: Optional[int] = Field(default=None, foreign_key="departamento.id")
    departamento: Optional[Departamento] = Relationship(back_populates="empleados")
    
    nominas: List["Nomina"] = Relationship(back_populates="empleado")

class Nomina(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    periodo_pago: str
    salario_base: float
    deducciones: float
    bonificaciones: float
    neto_pagar: float
    
    empleado_id: int = Field(foreign_key="empleado.id")
    empleado: Optional[Empleado] = Relationship(back_populates="nominas") 

class Cargo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nom_puesto: str
    salario_base: float
    niv_jerarquico: str
    descripcion: str
    estado: bool