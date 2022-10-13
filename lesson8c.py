# Bank Account
# properties -> balance, accno, name, branch, active
# methods -> check_balnce(), deposit(), withdraw, get_loan()

# inheritance
# polymorphism
# encapsulation
# Exception Handling

# Databases -> A collection of tables with records
# C -> Creating a database/table, storing data
# R -> Retrieve data from the data
# U -> Update the data
# D -> Delete the data

# MySQL, Oracle, SQLite, Postgesql...
# pymysql library/module
# Xampp/phpMyadmin database interface

class Account:
    bank_code = 1000

    def __init__(self, balance, accno, name, branch, status):
        if balance < 0:
            print("Balance Cannot be Zero")
        elif len(name) == 0:
            print("Please Enter Your Name")
        elif len(accno) != 5:
            print("Invalid Acc NO")
        else:
            print("Bank Details Captured")
            self.balance = balance
            self.accno = accno
            self.name = name
            self.branch = branch
            self.status = status

    def check_balance(self):
        print(f'Your balnce is {self.balance}')
        return self.balance

    def deposit(self, amount_to_deposit):
        if amount_to_deposit <= 0:
            print("Cannot deposit Zero or Negative Amount")

        elif amount_to_deposit > 70000:
            print("Exceeded the Maximum Deposit Amount")

        else:
            if self.status == "active":
                print("Thank You for Depositing with Us")
                print(f'Your Previous Balance was {self.check_balance()}')
                self.balance = self.balance + amount_to_deposit
                print(f'Your Current Balance is {self.balance}')
                return self.balance

            else:
                print("Your Account is Inactive")

    # Create a method to withdraw Amount
    # Cannot withdraw more that what is in the account
    # Account is Inactive

    # Exception Handling in Python

    # Should retain an anitial deposit = 100
    def withdraw(self):
        INITIAL_DEPOSIT = 100
        amount_to_widthdraw = int(input("Enter the Amount to withdraw...: "))

        if amount_to_widthdraw > self.balance:
            print("The Amount Exceeds Balance in the Account")
        elif (self.balance-amount_to_widthdraw) < INITIAL_DEPOSIT:
            print("You should retain an initial deposit of 100Ksh")
        else:
            if self.status == "active":
                print("Thank You for widthdrawing...")
                print("You have withdrawn {}".format(amount_to_widthdraw))
                self.balance = self.balance - amount_to_widthdraw
                print("Your current Balance is now {}".format(self.balance))
                return self.balance
            else:
                print("Visit Nearest Branch to activate Your Account")


account = Account(100, "12345", "Erick Otieno", "Westlands", "active")

account.check_balance()
account.deposit(10000)
account.withdraw()
