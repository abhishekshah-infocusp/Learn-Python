from dataclasses import asdict, astuple, dataclass, field, fields
from day_30_04_2025_dataclasses.circle_regular import Circle_Regular as CR
from day_30_04_2025_dataclasses.circle_dataclass import Circle_Dataclass as CD
from day_30_04_2025_dataclasses.circle_regular_immutable import Circle_Regular_Immutable as CRI
from day_30_04_2025_dataclasses.circle_dataclass_immutable import Circle_Dataclass_Immutable as CDI
from day_30_04_2025_dataclasses.circle_dataclass_postinit import Circle_DataclassPostInit as CDP

print("-------------------------------------------String Repr-----------------------------------------------")
print("Circle Class (Regular):")
c = CR(1, 2, 3)
print(c)       

print("\nCircle Class (Dataclass):")
c_dataclass = CD(x=1, y=2, radius=3)
print(c_dataclass)

# We can modify the values of the dataclass instances as well same as the regular class
c_dataclass.x = 100
c_dataclass.y = 200
print("Circle_Dataclass: ", c_dataclass)

print("\n\n-------------------------------------------Equality--------------------------------------------------")

print("Circle Class (Regular):")
c1 = CR(1, 2, 3)
c2 = CR(1, 2, 3)
print("comparision using ==: ", c1 == c2) # It will use custom __eq__ method
print("comparision using __eq__: ", c1.__eq__(c2)) # It will use custom __eq__ method
print("comparision using is: ", c1 is c2)  # NOT SAME OBJECT
print("comparision using id: ", id(c1) == id(c2)) # NOT SAME OBJECT

print("\nCircle Class (Dataclass):")
c1_dataclass = CD(1, 2, 3)
c2_dataclass = CD(1, 2, 3)
print("comparision using ==: ", c1_dataclass == c2_dataclass) # it will use inbuilt __eq__ method
print("comparision using __eq__: ", c1_dataclass.__eq__(c2_dataclass)) #it will use inbuilt __eq__ method
print("comparision using is: ", c1_dataclass is c2_dataclass) # NOT SAME OBJECT
print("comparision using id: ", id(c1_dataclass) == id(c2_dataclass)) # NOT SAME OBJECT


print("\n\n-------------------------------------------Hashing--------------------------------------------------")
print("Circle Class (Regular):")
c1 = CR(1, 2, 3)
c2 = CR(1, 2, 3)
print("Hash of c1: ", hash(c1)) # It will use custom __hash__ method
print("Hash of c2: ", hash(c2)) # It will use custom __hash__ method
print("Hash of c1 == Hash of c2: ", hash(c1) == hash(c2)) # It will use custom __hash__ method

print("\nCircle Class (Dataclass):")
print("By default data classes are not hashbale")
print("If we want to hash the dataclass, we need to set frozen=True in the dataclass decorator and make that class not immutable")

c1_dataclass_hashable = CDI(1, 2, 3)
c2_dataclass_hashable = CDI(1, 2, 3)
print("Hash of c1_dataclass_hashable: ", hash(c1_dataclass_hashable)) # It will use inbuilt __hash__ method
print("Hash of c2_dataclass_hashable: ", hash(c2_dataclass_hashable)) # It will use inbuilt __hash__ method
print("Hash of c1_dataclass_hashable == Hash of c2_dataclass_hashable: ", hash(c1_dataclass_hashable) == hash(c2_dataclass_hashable)) # It will use inbuilt __hash__ method
# print(c1_dataclass == c2_dataclass, hash(c1_dataclass) == hash(c2_dataclass), c1_dataclass is c2_dataclass, id(c1_dataclass) == id(c2_dataclass))

print("\n\n-------------------------------------------Immutability -----------------------------------------------")
print("Circle Class (Regular):")
c1 = CR(1, 2, 3)
c2 = CR(1, 2, 3)
print("Before changing the values of c1: ", c1)
print(c1 == c2, hash(c1) == hash(c2), c1 is c2, id(c1) == id(c2))
c1.x = 100
c1.y = 200
print("After changing the values of c1: ", c1)
print(c1 == c2, hash(c1) == hash(c2), c1 is c2, id(c1) == id(c2))

print("\nCircle Class (Dataclass):")
c1_dataclass = CD(1, 2, 3)
c2_dataclass = CD(1, 2, 3)
print("Before changing the values of c1_dataclass: ", c1_dataclass)
c1_dataclass.x = 100
c1_dataclass.y = 200
print("After changing the values of c1_dataclass: ", c1_dataclass)
print("Before changing the values of c2_dataclass: ", c2_dataclass)
c2_dataclass.x = 100
c2_dataclass.y = 200
print("After changing the values of c2_dataclass: ", c2_dataclass)

print("\n\n-------------------------------------------Ordering -----------------------------------------------")
print("Circle Class (Regular):")
c1 = CR(2, 3, 4)
c2 = CR(1, 2, 3)
print("Comparision using < : ", c1 < c2) # It will use custom __lt__ method
print("Comparision using __lt__ : ", c1.__lt__(c2)) # It will use custom __lt__ method
print("Comparision using > : ", c1 > c2) # It will use custom __lt__ method

print("\nCircle Class (Dataclass):")
c1_dataclass = CD(2, 3, 4)
c2_dataclass = CD(1, 2, 3)
print("Comparision using < : ", c1_dataclass < c2_dataclass) # It will use inbuilt __lt__ method
print("Comparision using __lt__ : ", c1_dataclass.__lt__(c2_dataclass)) # It will use inbuilt __lt__ method


print("\n\n-------------------------------------------Serialization -----------------------------------------------")
print("Circle Class (Regular):")
print("Converting object to dictionary: ", c.asdict())
print("Converting object to tuple: ", c.astupple())

print("\nCircle Class (Dataclass):")
print("Converting dataclass to dictionary: ", asdict(c_dataclass))
print("Converting dataclass to tuple: ", astuple(c_dataclass))


print("\n\n-------------------------------------------Fields Introspection -----------------------------------------------")
print("Circle Class (Dataclass):")
for ff in fields(c_dataclass):
    print(ff, end="\n----------------------\n")

print("\n\n-------------------------------------------Custom Methods and Properties -----------------------------------------------")
print("Circle Class (Dataclass):")
print(c_dataclass.area)
print(c_dataclass.circumference())

print("\n\n-------------------------------------------Override the default Order -----------------------------------------------")
print("Circle Class (Dataclass)):")
c1_dataclass = CD(1, 2, 3)
c2_dataclass = CD(2, 3, 4)
print("Comparision using < : ", c1_dataclass < c2_dataclass) # It will use custom __lt__ method
print("Comparision using __lt__ : ", c1_dataclass.__lt__(c2_dataclass)) # It will use custom __lt__ method

print("\n\n-------------------------------------------Post INIT & Initiation VAR----------------------------------------------")
Circle_DataclassPostInit = CDP(1, 2, 3, translate_x=4, translate_y=5)
print(Circle_DataclassPostInit)
print(asdict(Circle_DataclassPostInit))

print("\n\n-------------------------------------------Field Level Customisations----------------------------------------------")
print(c_dataclass) # As the repr is set to false for radius, it will not be printed

print("\n\n-------------------------------------------Non Initialised Fields----------------------------------------------")
c_dataclass = CDP(1, 2, 3, translate_x=4, translate_y=5)
print(c_dataclass.area)

for ff in fields(c_dataclass):
    print(ff, end="\n----------------------\n")

print(c_dataclass.__dict__)

print("This will not work if frozen is set to True as we are trying to change the atrributet value in postinit")


print("\n\n-------------------------------------------Customized field comparision----------------------------------------------")
c1_dataclass = CD(1, 2, 3)
c2_dataclass = CD(2, 4, 3)
print("Check Equality: ", c1_dataclass == c2_dataclass) # it will compare only those fields where compare is set to True

print("\n\n-------------------------------------------Customized hashing and mutability----------------------------------------------")
# from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Person:
    ssn: str
    name: str = field(compare=False)
    age: int = field(compare=False)

p1 = Person("John", 25, "123-45-6789")
p2 = Person("John", 25, "123-45-67")
p3 = Person("John", 25, "123-45-6789")

print(p1 == p2, p2 == p3, p1 == p3, p1 < p2)
print(hash(p1), hash(p2), hash(p3))

print("\n\n-------------------------------------------Unsafe Hash----------------------------------------------")
@dataclass(order=True, unsafe_hash=True)
class Person:
    ssn: str
    name: str = field(compare=False)
    age: int = field(compare=False)

p1 = Person("John", 25, "123-45-6789")
print(hash(p1))
# print(hash(print(p1)))

print("\n\n-------------------------------------------KW ONLY Another way----------------------------------------------")

@dataclass
class Person:
    name: str = "Unknown"
    age: int = 0
    ssn: str = field(default="Unknown", kw_only=True)

p1 = Person("John", 25, ssn="123-45-6789")
print(p1)

print("\n\n-------------------------------------------Custom Metadata----------------------------------------------")

@dataclass
class Person:
    name: str = field(default="Unknown", metadata ={"description": "Name of the person"})
    age: int = field(default=0, metadata = {"description": "Age of the person"})
    ssn: str = field(default="Unknown", kw_only=True,metadata={"description": "SSN of the person"})

p1 = Person("John", 25, ssn="123-45-6789")
print(fields(p1))

print("\n\n-------------------------------------------Default Factory----------------------------------------------")

@dataclass
class Test:
    test_list: list = field(default_factory = list)

    def add(self, item):
        self.test_list.append(item)

t1 = Test()
t1.add(1)
t1.add(2)
print(t1.test_list)
t2 = Test()
t2.add(3)
t2.add(4)
print(t2.test_list)

