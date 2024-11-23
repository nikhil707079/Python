# Class to represent a customer
class Customer:
    def __init__(self, name, customer_id):
        name = input("Enter your name: ")
        id =input("Enter customer_id :") 
        balance = input("Enter balance :")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.name}'s account. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s account. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} from {self.name}'s account to {recipient.name}'s account.")
            print(f"New balance for {self.name}: ${self.balance}")
            print(f"New balance for {recipient.name}: ${recipient.balance}")
        else:
            print("Insufficient funds or invalid transfer amount.")

# Class to represent the bank system
class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name):
        customer_id = len(self.customers) + 1
        new_customer = Customer(name, customer_id)
        self.customers[customer_id] = new_customer
        print(f"Added new customer: {name} with customer ID: {customer_id}")
        return new_customer

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def customer_summary(self):
        print("Customer Summary:")
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Balance: ${customer.balance}")

# Simulating the banking system
bank = Bank()

# Add some customers
#customer1 = bank.add_customer("Alice")
#customer2 = bank.add_customer("Bob")

## Make some transactions
##customer1.deposit(1000)
##customer2.deposit(500)
##customer1.withdraw(200)
##customer1.transfer(300, customer2)

 Print a summary of all customers
 bank.customer_summary()
