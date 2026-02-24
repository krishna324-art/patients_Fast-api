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
patient1=Patient(**patient_dict)
print(patient1.name)
print(patient1.age)
print(patient1.email)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.country)


#better organization of related data
#reusability:use vitals in multiple models
#redability;easier for developers to understand the structure of the data
#validation:nested models are validated automatically when the parent model is validated, ensuring data integrity and consistency across the entire data structure.
