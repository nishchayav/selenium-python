
'''Question – Introduction to OOPs, Classes & Objects
Create a class Student that:
1. Has attributes name and roll_no
2. Has a method display_details() to print student information
3. Create at least two objects of the class and display their details'''


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


stu1 = Student("Nish", 101)
stu2 = Student("Vish", 102)

stu1.display_details()
print()
stu2.display_details()




'''Question – Parameterized Methods, Constructors & Destructors 
Create a class BankAccount that: 
1. Uses a parameterized constructor to initialize account_number and balance 
2. Implements methods deposit(amount) and withdraw(amount) 
3. Uses a destructor to display a message when the object is deleted 
4. Handle invalid withdrawal using proper checks'''


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} your new updated balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} you updated remaining balance: {self.balance}")

    def __del__(self):
        print(f"Account {self.account_number} is being deleted")



account1 = BankAccount(7581, 100)

account1.deposit(120)
account1.withdraw(220)
account1.withdraw(100)   # Invalid withdrawal
