from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import ItemCreate, ItemUpdate, ItemResponse, PatientResponse, DoctorResponse
from crud import create_item, get_items, get_item, update_item, delete_item
import crud, schemas
from models import Doctor, Patient
from typing import Optional

app = FastAPI(
    title="FastAPI Hospital API",
    description="An API for managing doctors and patients.",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


# Routes for items
@app.post("/items/", response_model=ItemResponse)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@app.get("/items/", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return get_items(db)

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_existing_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}


# Routes for doctor
@app.post("/doctors/", response_model=schemas.DoctorResponse)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@app.get("/doctors/", response_model=list[schemas.DoctorResponse])
def get_all_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_doctors(db, skip, limit)

@app.get("/doctors/{doctor_id}", response_model=schemas.DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.put("/doctors/{doctor_id}", response_model=schemas.DoctorResponse)
def update_doctor(doctor_id: int, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    updated_doctor = crud.update_doctor(db, doctor_id, doctor)
    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated_doctor  

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    deleted_doctor = crud.delete_doctor(db, doctor_id)
    if not deleted_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}


# Routes for Patient
@app.post("/patients/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model=list[schemas.PatientResponse])
def get_all_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_patients(db, skip, limit)

@app.get("/patients/{patient_id}", response_model=schemas.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.put("/patients/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(patient_id: int, patient_update: schemas.PatientUpdate, db: Session = Depends(get_db)):
    updated_patient = crud.update_patient(db, patient_id, patient_update)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted_patient = crud.delete_patient(db, patient_id)
    if not deleted_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}


# Search patients by name
@app.get("/search-patients/search", response_model=list[PatientResponse])
def search_patients(name: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Patient)
    if name:
        query = query.filter(Patient.name.ilike(f"%{name}%"))
    
    patients = query.all()
    return patients


# Search doctors by name
@app.get("/search-doctors/search", response_model=list[DoctorResponse])
def search_doctors(name: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Doctor)
    if name:
        query = query.filter(Doctor.name.ilike(f"%{name}%"))

    doctors = query.all()
    return doctors