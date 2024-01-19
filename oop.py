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
    

#Instantiating Dog object
doggo = Dog("Mikey", 6);

print(doggo.description());
print(doggo.speak("Woof Woof!"))
print(doggo.bite(3));
    


# my_dog = Dog("Snoopy",8)
# print(my_dog.name);
# print(my_dog.age);