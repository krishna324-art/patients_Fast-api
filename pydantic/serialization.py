from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    country: str
    pin:str
class Patient(BaseModel):
    name: str
    age: int
    email: str
    address:Address
    weight: float
    linkedin_url: str
    married: bool
    allergies: list[str]
    contact_details: dict
address_dict={'city':'Ahmedabad','state':'Gujarat','country':'India','pin':'380015'}
address1=Address(**address_dict)
patient_dict={
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com',
    'address': address1,
    'weight': 70.5,
    'linkedin_url': 'http://linkedin.com/in/johndoe',
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '1234567890'}
}
Patient1=Patient(**patient_dict)
temp=Patient1.model_dump(include=['name','age','email'])#converts existing pydantic model  to dictionary
print(temp)
print(type(temp))

