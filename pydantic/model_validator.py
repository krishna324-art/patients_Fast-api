from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator
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
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
             raise ValueError('patients older than 60 must have an emergency contact')
        return model
    
def update_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.linkedin_url)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
patient_info = {
    'name': 'John Doe',
    'age': '65',
    'email': 'abc@hdfc.com',  # Changed to valid domain
    'linkedin_url': 'http://linkedin.com/1322',
    'weight': 70.5,  # Pass as float, not string
    'contact_details': {'phone': '9619460043','emergency':'235236'}
}
patient1 = Patient(**patient_info)#VALIDATION HAPPENS HERE,TYPE COERSION

update_patient_data(patient1)