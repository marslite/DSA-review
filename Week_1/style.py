
# in the function greeting, the argument name is expected to be of type str and the return type str.
# Subtypes are accepted as arguments

def greeting(name:str) -> str:
    return "Hello" + name;

#This function accepts a list of integers as an argument and returns a list of integers as output
def double_list(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] * 2
    return nums

#This function accepts a list of integers as an argument and returns an integer
def sum_list(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num
        ##To alert about a possible BUG

    return total

##To alert about a possible BUG
Vector = list[int]
def multiply_list(vector: Vector, multiplier: int=2) -> Vector:
    for i in range(len(vector)):
        vector[i] = vector[i] * multiplier
    return vector

class CoachableStudent:
    #The :str after name means we are expecting the first argument to be of type str, aka a string
    #For :int after age means we are expecting age to be of type integer

    def __init__(self,name: str, age:int):
        self.name = name
        self.age = age
        #The -> None after the fucntion declaration means that it will return None (nothing)
    def change_name(self, new_name:str) -> None:
        self._name = new_name

    def say_hello(self) -> None:
        print("Hello!")

    def get_age(self) -> int:
        return self.age
    
    def make_intro(self) ->str:
        return f"Hi I'm {self.name} and I'm {self.age} y.o"


student = CoachableStudent("Mattia",26)
print(student.make_intro());


i = 0;
nums = [1,2,4,4]

# while i < len(nums):
#     print(key, "-", )
#     key = 2 - nums[i]
#     if key in nums:
#         nums[key] += 3

#     # nums[nums[i]] = i
#     i +=1;

# print(nums);

def doSomething(nums):
    for i,num in enumerate(nums):
        print(i,num)
    


    

print(doSomething(nums));


# if key in nums:
#     print()

l1 = [10,10,10];

# print(double_list(l1));
# print(multiply_list(l1));