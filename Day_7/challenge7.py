# Improvement upon code that I need to do is to make it such that it retains information on accounts that I can further withdraw from

from random import randint

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):
    
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name,last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAccount number: {self.account_number}\nAccount balance: ${self.balance}."

    def deposit(self,add_money):
        self.balance += add_money

    def withdraw(self,take_money):
        self.balance -= take_money


def create_client():
    first_name = input("What is the client's first name? ")
    last_name = input("What is the client's last name? ")
    account_number = randint(900000,999999)
    balance = randint(999,9999)

    return Customer(first_name,last_name,account_number,balance)

def bank_ops():
    client = create_client()
    print(client)

    while True:
        choice = int(input("What operation would you like to perform\n1. Deposit\n2. Withdraw\n3. Exit Program\n"))
        if choice == 1:
            amount = int(input("How much do you want to deposit? "))
            client.deposit(amount)
            print(client)
        elif choice == 2:
            amount = int(input("How much do you want to withdraw? "))
            client.withdraw(amount)
            print(client)
        else:
            print(client)
            break

bank_ops()




# asaah = Customer('Asaah','Ndangoh',9999,969)

# asaah.withdraw(69)

# print(asaah)