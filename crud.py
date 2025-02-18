from sqlalchemy.orm import Session
from models import Item, Doctor, Patient
from schemas import ItemCreate, ItemUpdate, DoctorCreate, PatientCreate, PatientUpdate


# CRUD operations for Item
def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: Session, item_id: int, item: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item


# CRUD operations for Doctor
def create_doctor(db:Session, doctor:DoctorCreate):
    new_doctor = Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

def get_doctors(db:Session, skip: int = 0, limit: int = 15):
    return db.query(Doctor).offset(skip).limit(limit).all()

def get_doctor(db:Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def update_doctor(db:Session, doctor_id: int, doctor_update: DoctorCreate):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if doctor:
        for key, value in doctor_update.model_dump().items():
            setattr(doctor, key, value)
        db.commit()
        db.refresh(doctor)
    return doctor

def delete_doctor(db:Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if doctor:
        db.delete(doctor)
        db.commit()
    return doctor


# CRUD operations for Patient
def create_patient(db:Session, patient:PatientCreate):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Patient).offset(skip).limit(limit).all()

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def update_patient(db: Session, patient_id: int, patient_update: PatientUpdate):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return None 

    update_data = patient_update.model_dump(exclude_unset=True)  
    for key, value in update_data.items():
        setattr(patient, key, value)  

    db.commit()
    db.refresh(patient) 
    return patient

def delete_patient(db: Session, patiend_id: int):
    patient = db.query(Patient).filter(Patient.id == patiend_id).first()

    if patient:
        db.delete(patient)
        db.commit()
    return patient
