from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # pydantic model
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='give the name of the patient in less than 50 characters')]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=150)  # defining the range
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool = False
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_detials: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError('Invalid email domain')
        return value 
    @field_validator('name',mode="after")
    @ classmethod
    def transform_name(cls,value):
         return value.upper()

    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
       if 0<value<100:
            return value
       else:
            raise ValueError('Invalid age')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.linkedin_url)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detials)
    print('updated')


patient_info = {
    'name': 'John Doe',
    'age': 30,
    'email': 'abc@hdfc.com',  # Changed to valid domain
    'linkedin_url': 'http://linkedin.com/1322',
    'weight': 70.5,  # Pass as float, not string
    'contact_detials': {'phone': '9619460043'}
}

patient1 = Patient(**patient_info)#VALIDATION HAPPENS HERE,TYPE COERSION

update_patient_data(patient1)
