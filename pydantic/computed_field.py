from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator,computed_field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    # pydantic model
    name:str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight:float#kg
    height:float#mtr
    married:bool
    allergies:list[str]
    contact_details: Dict[str, str]
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

# Move update_patient_data outside the class and fix indentation
def update_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.linkedin_url)
    print(patient.married)
    print('BMI', patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
patient_info = {
    'name': 'John Doe',
    'age': '65',
    'email': 'abc@hdfc.com',  
    'linkedin_url': 'http://linkedin.com/1322',
    'weight': 70.5,  
    'height':1.75,
    'married':True,
    'allergies':['pollen','dust'],
    'contact_details': {'phone': '9619460043','emergency':'235236'}
}
patient1 = Patient(**patient_info)#VALIDATION HAPPENS HERE,TYPE COERSION
update_patient_data(patient1)

