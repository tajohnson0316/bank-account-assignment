class User:
    def __init__(self, name="John/Jane Doe", email="user@noemail.com"):
        self.name = name
        self.email = email
        self.total_accounts = 1
        self.account = BankAccount(
            self.total_accounts,
            interest_rate=0.02,
            balance=0,
        )
        self.accounts = [self.account]

    def make_deposit(self, amount, account_number=1):
        if account_number > len(self.accounts) or account_number <= 0:
            print(f"Error: Please enter a valid account number")
        else:
            print(f"{self.name.upper()} - ACCOUNT #{account_number}")
            self.accounts[account_number - 1].deposit(amount)

    def make_withdrawal(self, amount, account_number=1):
        if account_number > len(self.accounts) or account_number <= 0:
            print(f"Error: Please enter a valid account number")
        else:
            print(f"{self.name.upper()} - ACCOUNT #{account_number}")
            self.accounts[account_number - 1].withdraw(amount)

    def yielded_interest(self, account_number=1):
        if account_number > len(self.accounts) or account_number <= 0:
            print(f"Error: Please enter a valid account number")
        else:
            print(f"{self.name.upper()} - ACCOUNT #{account_number}")
            self.accounts[account_number - 1].yield_interest()

    def display_user_balance(self, account_number=1):
        if account_number > len(self.accounts) or account_number <= 0:
            print(f"Error: Please enter a valid account number")
        else:
            print(f"{self.name.upper()} - ACCOUNT #{account_number}")
            self.accounts[account_number - 1].display_account_info()

    def add_account(self, interest_rate=0.0, balance=0):
        self.total_accounts += 1
        self.accounts.append(BankAccount(self.total_accounts, interest_rate, balance))
        
    def transfer_funds(self, amount, other_user = None, account_number = 1):
        if (other_user == None):
            print("Error: Please specify a user to transfer funds.")
            return
        if (amount <= 0):
            print("Error: You may only transfer non-zero/non-negative amounts.")
            return
            
        other_user.make_deposit(amount)
        self.make_withdrawal(amount, account_number)
        print("Transfer successful")
        


class BankAccount:
    def __init__(self, account_number=1, interest_rate=0.0, balance=0):
        if interest_rate < 0:
            print("Error: Interest rate must be a non-negative value")
        else:
            self.interest_rate = interest_rate

        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Please deposit an amount greater than $0")
        else:
            previous_balance = self.balance
            self.balance += amount
            print(f"Thank you for your deposit of ${amount}")
            print("Previous balance: $", format(previous_balance, ",.2f"))
            print("Final balance: $", format(self.balance, ",.2f"))
            print("- - - - - - - - - - - - - - - - - - - -")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Please withdraw an amount greater than $0")
        else:
            previous_balance = self.balance
            self.balance -= amount
            if self.balance < 0:
                print("Insufficient funds: Charging a $5 fee.")
                self.balance -= 5
            print(f"Thank you for your withdrawal of ${amount}")
            print("Previous balance: $", format(previous_balance, ",.2f"))
            print("Final balance: $", format(self.balance, ",.2f"))
            print("- - - - - - - - - - - - - - - - - - - -")

    def display_account_info(self):
        print("ACCOUNT INFORMATION:")
        print("Account balance: $", format(self.balance, ",.2f"))
        print("Current Interest Rate:", format(self.interest_rate * 100, ".2f"), "%")
        print("- - - - - - - - - - - - - - - - - - - -")

    def yield_interest(self):
        if self.balance < 0:
            print("Error: Must have a non-negative balance to yield interest")
            print("Current balance: $", format(self.balance, ",.2f"))
            print("- - - - - - - - - - - - - - - - - - - -")
        else:
            previous_balance = self.balance
            self.balance += self.balance * self.interest_rate
            print("Previous balance: $", format(previous_balance, ",.2f"))
            print("Final balance: $", format(self.balance, ",.2f"))
            print("- - - - - - - - - - - - - - - - - - - -")


""" account_1 = BankAccount(0.08, 100)
account_2 = BankAccount(0.02, 1000)

account_1.deposit(200), account_1.deposit(50), account_1.deposit(1200),
account_1.withdraw(500),
account_1.yield_interest(),
account_1.display_account_info()

account_2.deposit(1000), account_2.deposit(15000),
account_2.withdraw(500), account_2.withdraw(250), account_2.withdraw(1000), account_2.withdraw(20000)
account_2.yield_interest(),
account_2.display_account_info() """

user_1 = User("Timothy Johnson", "tajohnson0316@gmail.com")
user_2 = User()

user_1.make_deposit(200), user_1.make_deposit(50), user_1.make_deposit(1200),
user_1.make_withdrawal(500),
user_1.yielded_interest(),
user_1.display_user_balance(),
user_1.transfer_funds(500, user_2)
