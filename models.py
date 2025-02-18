from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    patients = relationship("Patient", back_populates="doctor", cascade="all, delete")


class Patient(Base):
    __tablename__ = "patients"

    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    condition = Column(String, nullable=True)

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    doctor = relationship("Doctor", back_populates="patients")
