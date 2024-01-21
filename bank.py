
class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Funds")
        else:
            self.__balance -= amount



mattia = BankAccount();
print(mattia.get_balance());
mattia.deposit(10)
print(mattia.get_balance());
mattia.withdraw(5);
print(mattia.get_balance());
