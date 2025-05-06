from day_01_05_2025_pydantic.person import Person
from pydantic import ValidationError, Field # type: ignore
import json
from day_01_05_2025_pydantic.employee import Employee

print("\n\n-------------------------------------------Basic Models----------------------------------------------")
p1 = Person(name="Abhishek", age=26, email="abhishek.shah@infocusp.com")
print("Pydantic Person Object:")
print(p1)

p2 = Person(name ="Abhishek", age ="26", email ="p2@infocusp.com")
print("\nAfter providing wrong type of age:")
print(p2)

# This will raise a validation error
#print("\nAfter providing wrong type of age:")
#p3 = Person(name ="Abhishek", age ="26dcz", email ="p2@infocusp.com")
#print(p3)

try:
    Person(name="Abhishek", age = "26dcz", email =45)
except Exception as e:
    print("Validation Error:")
    print(e)

print("\n\nWe can mutate the object:")
p1.name = "Abhi"
print(p1)

print("\n\n-------------------------------------------Validateion Exceptions----------------------------------------------")

try:
    Person(name="Abhishek", age = "26dcz", email =45)
except ValidationError as e:
    exceptions = e

print("\nValidation Exceptions:")
print(exceptions.errors())

print("\nValidation Exceptions in JSON format:")
print(exceptions.json())

print("\n\n--------------------------------------- Deserializing Data----------------------------------------------")

temp_data = {
    "name": "Abhishek",
    "age": 26,
    "email": "myemail@gmail.com"
}

p = Person.model_validate(temp_data)
print("\nDeserialized Data using dictionary:")
print(p)

temp_data = '''
{
    "name": "Abhishek",
    "age": 26,
    "email": "myemail@gmail.com"
}
'''
p = Person.model_validate_json(temp_data)
print("\nDeserialized Data using JSON:")
print(p)

print("\n\n-------------------------------------------Serialization----------------------------------------------")
print("\nSerialized Data using dictionary:")
print(p.model_dump())
print("\nSerialized Data using JSON:")
print(p.model_dump_json())
print("\nSerialized Data using JSON with indent:")
print(p.model_dump_json(indent=4))

json_schema = Person.model_json_schema()
print(type(json_schema))
preety_json_schema = json.dumps(json_schema, indent = 4)
print("\nJSON Schema:")
print(preety_json_schema)

print("\n\n-------------------------------------------Field Customisations Incorrect Input ----------------------------------------------")
print("\nWrong inputs with provided field customizations and restrictions:")

incorrect_employee_data = {
    "name": "",
    "email": "dummy@infocusp.com",
    "birth_date": "1998-04-02",
    "salary": -10,
    "department": "IT",
    "other_benifits": True,
}
try:
    e1 = Employee.model_validate(incorrect_employee_data)
    print("\n\nEmployee Object:")
    print(e1)
except Exception as e:
    print("\nValidation Error:")
    print(e)

print("\n\n-------------------------------------------Field Customisations Correct Input ----------------------------------------------")
correct_employee_data = {
    "name": "Abhishek Shah",
    "email": "abhishek.shah@infocusp.com",   
    "dob": "1998-06-15",                     
    "salary": 75000.0,                       
    "department": "IT",
    "other_benifits": True
}

e2 = Employee.model_validate(correct_employee_data)
print("\n\nEmployee Object:")
print(e2)
print("Salary: ", e2.salary)
print("DOB: ", e2.date_of_birth)


print("\n\n-------------------------------------------Custom Validator for DOB ----------------------------------------------")
employee_data = {
    "name": "Abhishek Shah",
    "email": "abhishek.shah@infocusp.com",   
    "dob": "2020-06-15",                     
    "salary": 75000.0,                       
    "department": "IT",
    "other_benifits": True
}

try:
    e = Employee.model_validate(employee_data)
except Exception as e:
    print("\nValidation Error:")
    print(e)



print("\n\n-------------------------------------------Custom Validator for model ----------------------------------------------")
employee_data = {
    "name": "Abhishek Shah",
    "email": "abhishek.shah@infocusp.com",   
    "dob": "1995-06-15",                     
    "salary": 75000.0,                       
    "department": "HR",
    "other_benifits": True
}

try:
    e = Employee.model_validate(employee_data)
except Exception as e:
    print("\nValidation Error:")
    print(e)

print("\n\n-------------------------------------------Custom Validator for Methods ----------------------------------------------")
print("\n\nCustom Validator for Methods:")
items = ["item1", "item2"]
amount = 100.0
employee_data = {
    "name": "Abhishek Shah",
    "email": "abhishek.shah@infocusp.com",   
    "dob": "1995-06-15",                     
    "salary": 75000.0,                       
    "department": "HR",
    "other_benifits": False
}

try:
    e = Employee.model_validate(employee_data)

except Exception as e:
    print("\nValidation Error:")
    print(e)

print("Successfully created employee object:")
print(e)

try:
    print(e.send_invoice(items_purchased = items,amount_owed = amount))
except Exception as e:
    print("\nValidation Error:")
    print(e)

