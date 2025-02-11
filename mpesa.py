from abc import ABC, abstractmethod


#Encapsulation
class Account:
    #constructor method
    def __init__(self,account_id,holder_name,balance):
        self.account_id=account_id
        self.holder_name=holder_name
        self.balance=balance
    #a method function
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited:{amount}.\n New Balance:{self.balance}")

    def withdraw(self,amount):
        print(f"Withdrawn:{amount}\n New Balance:{self.balance}")
        if amount<=self.balance:
            self.balance -=amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.balance
    def get_holder_name(self):
        return self.holder_name


#Inheritance
class Customer(Account):
    def __init__(self,account_id,holder_name,balance,phone_number):
        super().__init__(account_id,holder_name,balance)
        self.phone_number=phone_number


# polymorphism
class Transaction():
    def __init__(self,amount):
        self.amount=amount
    def execute(self,account):
        pass
class DepositTransaction(Transaction):
    def execute(self,account):
        account.deposit(self.amount)
class WithdrawTransaction(Transaction):
    def execute(self,account):
        account.withdraw(self.amount)


#Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_transaction(self,amount):
        pass
class MpesaPaymentSystem(PaymentSystem):
    def process_transaction(self,amount):
        print(f"Processing Mpesa payment of {amount}")

# Example usage
mpesa=MpesaPaymentSystem()
account1=Customer(1,"Sky Mwangi",
                  20000,750546697)
deposit=DepositTransaction(1000)
withdraw=WithdrawTransaction(3550)

deposit.execute(account1)
withdraw.execute(account1)

print(f"Balance for {account1.get_holder_name()} is:"
      f"{account1.get_balance()}\n")


account2=Customer(2,"Dylan Kipkorir",
                  300,743568809)
deposit=DepositTransaction(200000)
withdraw=WithdrawTransaction(1000000)


deposit.execute(account2)
withdraw.execute(account2)

print(f"Balance for {account2.get_holder_name()} is:"
      f"{account2.get_balance()}")



