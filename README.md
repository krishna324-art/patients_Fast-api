
# Patients FastAPI

A RESTful API for managing patient records, built with **FastAPI** and **Pydantic**. This project supports full CRUD operations and includes auto-computed health metrics like BMI and a health verdict — all with interactive API documentation out of the box.

---

## Features

-  **Create, Read, Update, Delete** patient records
-  **Computed fields** — BMI and health verdict calculated automatically
- **Sort patients** by height, weight, or BMI
-  **Pydantic validation** — strict input validation with clear error messages
-  **Interactive docs** — Swagger UI and ReDoc included automatically

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/krishna324-art/patients_Fast-api.git
cd patients_Fast-api

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic
```

### Running the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

---

##  API Documentation

Once the server is running, visit:

| Interface | URL |
|-----------|-----|
| Swagger UI | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| ReDoc | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

---

##  API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/patients` | Get all patient records |
| `GET` | `/patients/{id}` | Get a specific patient by ID |
| `POST` | `/patients` | Create a new patient record |
| `PUT` | `/patients/{id}` | Update an existing patient |
| `DELETE` | `/patients/{id}` | Delete a patient record |
| `GET` | `/patients/sort` | Sort patients by `height`, `weight`, or `bmi` |

---

##  Data Model

### Patient Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `str` | Unique patient identifier |
| `name` | `str` | Full name of the patient |
| `age` | `int` | Age of the patient |
| `height` | `float` | Height in meters |
| `weight` | `float` | Weight in kilograms |
| `bmi` | `float` | *(Computed)* Body Mass Index |
| `verdict` | `str` | *(Computed)* Health status based on BMI |

### Example Patient Record

```json
{
  "id": "P001",
  "name": "John Doe",
  "age": 30,
  "height": 1.75,
  "weight": 70.0,
  "bmi": 22.86,
  "verdict": "Normal"
}
```

### BMI Verdict Categories

| BMI Range | Verdict |
|-----------|---------|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25.0 – 29.9 | Overweight |
| ≥ 30.0 | Obese |

---

##  Project Structure

```
patients_Fast-api/
├── main.py               # FastAPI app, routes, and models
├── patients.json         # JSON file used as the data store
├── practice.py           # Scratch/practice file
├── pydantic/             # Pydantic learning examples
│   ├── _pydantic_why.py
│   ├── computed_field.py
│   ├── model_validator.py
│   ├── nested_models.py
│   └── serialization.py
├── .gitignore
└── README.md
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [Pydantic](https://docs.pydantic.dev/) | Data validation and settings |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| Python 3.10+ | Language |

---

## Learning Resources

The `pydantic/` folder contains standalone examples covering key Pydantic concepts:

- **`_pydantic_why.py`** — Why Pydantic over plain dicts
- **`computed_field.py`** — Auto-computed fields (like BMI)
- **`model_validator.py`** — Cross-field validation logic
- **`nested_models.py`** — Models within models
- **`serialization.py`** — Controlling JSON output format

---


## License

This project is open source and available under the [MIT License](LICENSE).

---

