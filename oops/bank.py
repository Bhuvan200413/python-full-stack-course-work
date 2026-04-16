from abc import ABC, abstractmethod

class BankAccount(ABC):
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    def check_balance(self):
        print("You can check your balance")
    
    def view_history(self):
        print("You can check out your transactions")


class SavingAccount(BankAccount):
    
    def deposit(self):
        print("upto 10L per account")
    
    def withdraw(self):
        print("Maintain minimum balance")