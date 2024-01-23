from __future__ import annotations


class oldPerson:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def __le__(self,other):
        return self.age <= other.age


class Person:
    def __init__(self,first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} "
    
    def __repr__(self) -> str:
        return f"Person('{self.first_name}', {self.last_name}, '{self.age}')"
    
    def __eq__(self, other:Person):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age
    
    def __lt__(self, other:Person):
        if self.last_name ==  other.last_name:
            return self.first_name < other.first_name
        return self.last_name < other.last_name
    
    def __le__(self, other:Person):
        if self.last_name == other.last_name:
            return self.first_name <= other.first_name
        return self.last_name < other.last_name
    
    def __gt__(self, other: Person):
        if self.last_name == other.last_name:
            return self.first_name > other.first_name
        return self.last_name > other.last_name
    
    def __ge__(self,other:Person):
        if self.last_name == other.last_name:
            return self.first_name >= other.first_name
        return self.last_name > other.last_name
    

persons = [Person("John","Doe",30), Person("Jane","Doe",28),Person("Jim","Smith",35), Person("Jane","Smith",32)]
sorted_persons =sorted(persons)

print("Sorted by last name and first name :");
for person in sorted_persons:
    print(person)




p1 = oldPerson("John",30)
p2 = oldPerson("Jane",25)

print(p1 <= p2); #False
print(p2 <= p2); #True