from pydantic import BaseModel, EmailStr
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True


# Base class for Doctor table
class DoctorBase(BaseModel):
    name: str
    speciality: str
    phone: Optional[str] = None
    email: EmailStr


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attibutes = True


# Base models for patients
class PatientBase(BaseModel):
    name: str
    age: int
    condition: Optional[str] = None
    doctor_id: int


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    condition: Optional[str] = None
    doctor_id: Optional[int] = None


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True