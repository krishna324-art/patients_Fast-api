Overview
This API allows you to:

Create patient records
View all patients or a specific patient
Update patient details
Delete patient records
Sort patients by height, weight, or BMI
It is built for learning/practice with FastAPI and Pydantic.

Features
CRUD endpoints for patients
Pydantic model validation
Computed fields:
bmi
verdict

Interactive API docs:
Swagger UI (/docs)
ReDoc (/redoc)

Tech Stack
Python 3.10+
FastAPI
Pydantic
Uvicorn

Project Structure
fastapi/
├─ main.py
├─ patients.json
├─ practice.py
├─ pydantic/
│  ├─ _pydantic_why.py
│  ├─ computed_field.py
│  ├─ model_validator.py
│  ├─ nested_models.py
│  └─ serialization.py
