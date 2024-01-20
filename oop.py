class Dog:
    # Class Attribute
    species = 'mammal'
    # Initializer/ Instance Attributes
    ##We use __init__() method to initilaize an object's initial attributes by giving them their default value or state.
    def __init__(self,name,age):
        self.name= name
        self.age = age

    #Instance Method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    
    #Instance method
    def speak(self,sound):
        return "{} says {}".format(self.name, sound)
    
    #Instance method
    def bite(self, times):
        return "{} bites {} times!".format(self.name, times)


class Cat:
    def __init__(self,name,age):
        self._name = name
        self._age =  age

    def description(self):
        return "{} is {} years old".format(self._name ,self._age)
    

    

def makeCopy(lst):
    new_list = []
    _makeCopy(lst, new_list,0)
    return new_list


def _makeCopy(original_list, new_list, current_index):
    if current_index == len(original_list):
        return
    
    #adding element at index current_index to new list
    new_list.append(original_list[current_index])
    #moving current_index to next_element in original list
    _makeCopy(original_list,new_list,current_index +1)

lst = [1,2,3]
copy = makeCopy(lst);
print(lst);
print(copy);
print("is lst and copy the (==) the same list?", copy == lst);
print("is copy and lst share the same address in the memory aka same exact list pointing to each other, or different?", copy is lst);

#Instantiating Dog object
# doggo = Dog("Mikey", 6);

# print(doggo.description());
# print(doggo.speak("Woof Woof!"))
# print(doggo.bite(3));

# catto = Cat("Johnny",12);
# print(catto.description());
    


# my_dog = Dog("Snoopy",8)
# print(my_dog.name);
# print(my_dog.age);