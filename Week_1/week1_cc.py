import time 

class Customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    #It won't be able to represent any customer data untill we define __repr__ to 
    # convert  <__main__.Customer object at 0x10061ab90> into humanly-readable data
    def __repr__(self) -> str:
        return f"Customer: {self.name}, {self.age} yo"

class LunchLine:
    def __init__(self, customers: list[Customer], time_end: int) -> None:
        self.time_end = time_end
        #the line_size attributes shares the same name with the method "line_size"
        #so I renamed line_size to get_line_size(self)
        self.line_size = len(customers)
        self.customers = customers
    #In this way there would not be conflict between the attribute and the method.
    def get_line_size(self) -> int :
        return f"{self.line_size}"
    
    def __str__(self):
        return self.line_size
    


        
    def get_customers(self) -> list[Customer]:
        return self.customers

    def is_lunch_over(self) -> bool:
        current_time = time.time()
        if current_time > self.time_end:
            return True
        return False
      
c1 = Customer("Annie", 29)
c2 = Customer("Bob", 26)
c3 = Customer("Charlie", 29)
c4 = Customer("Dana", 35)
my_list = []
my_list.append(c1)
my_list.append(c2)
my_list.append(c3)
my_list.append(c4)
lunchline = LunchLine(my_list, 24)
check = lunchline.get_line_size();
#Also here I made it possible to see the lunchline size as a string by using __str__
# print(str(lunchline))
print(check);

for customer in lunchline.get_customers():
  print(customer)