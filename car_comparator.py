from typing import List

class Car:
    def __init__(self, make:str, model:str, year:int, speed:int, price:float):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.price = price

    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return  f"Car '{self.make}, {self.model}, {self.year}, {self.speed}, {self.price}'"
    
    def __eq__(self,other):
        if isinstance(other, Car):
            return self.year == other.year
        return NotImplemented
    
    def __lt__(self,other):
        if isinstance(other, Car):
            return self.price < other.price
        return NotImplemented
    

class CarDealer:
    def __init__(self, cars: List[Car]):
        self.cars = cars

    def __str__(self):
        return f"Car dealer with {len(self.cars)} cars"
    
    def __repr__(self):
        cars_repr = ', '.join([repr(c) for c in self.cars ])
        return f"CarDealer([{cars_repr}])"
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index:int):
        return self.cars[index]
    
    def add(self, car: Car):
        self.cars.append(car)

    def remove(self, car:Car):
        self.cars.remove(car);

    def __eq__(self, other):
        if isinstance(other, CarDealer):
            return self.cars == other.cars
        return NotImplemented
    
    def __lt__(self,other):
        if isinstance(other, CarDealer):
            return len(self.cars) < len(other.cars)
        return NotImplemented
    


my_car = Car("Toyota","Prius X",2020, 50, 35000.0)
your_car = Car ("Honda", "HRV", 2012, 40, 25000.0)
their_car = Car("Tesla", "Model S", 2023, 100, 90000.0)

our_cars = [my_car, your_car]
dealer = CarDealer(our_cars)
dealer.add(their_car);
dealer.remove(their_car);

print(str(dealer));
print(repr(dealer));
print(len(dealer));
print(dealer[0]);

other_dealer = CarDealer([my_car, your_car,their_car])

print(dealer == other_dealer);
