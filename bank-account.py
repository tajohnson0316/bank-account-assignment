class BankAccount:
    def __init__(self, interest_rate = 0.0, balance = 0):
        
        if (interest_rate < 0):
            print("Error: Interest rate must be a non-negative value")
        else:
            self.interest_rate = interest_rate
            
        self.balance = balance
        
    def deposit(self, amount):
        if (amount <= 0):
            print("Error: Please deposit an amount greater than $0")
        else:
            previous_balance = self.balance
            self.balance += amount
            print(f"Thank you for your deposit of ${amount}")
            print(f"Previous balance: ${previous_balance}")
            print(f"Final balance: ${self.balance}")
            print("- - - - - - - - - - - - - - - - - - - -")
        
    def withdraw(self, amount):
        if (amount <= 0):
            print("Error: Please withdraw an amount greater than $0")
        else:
            previous_balance = self.balance
            self.balance -= amount
            if (self.balance < 0):
                print("Insufficient funds: Charging a $5 fee.")
                self.balance -= 5
            print(f"Thank you for your withdrawal of ${amount}")
            print(f"Previous balance: ${previous_balance}")
            print(f"Final balance: ${self.balance}")
            print("- - - - - - - - - - - - - - - - - - - -")
    
    def display_account_info(self):
        print("ACCOUNT INFORMATION")
        print(f"Account Balance: ${self.balance}")
        print(f"Current Interest Rate: {self.interest_rate * 100}%")
        print("- - - - - - - - - - - - - - - - - - - -")
        
    def yield_interest(self):
        if (self.balance < 0):
            print("Error: Must have a non-negative balance to yield interest")
            print(f"Current balance: ${self.balance}")
            print("- - - - - - - - - - - - - - - - - - - -")
        else:
            previous_balance = self.balance
            self.balance += self.balance * self.interest_rate
            print(f"Previous balance: ${previous_balance}")
            print(f"Final balance after interest yield: ${self.balance}")
            print("- - - - - - - - - - - - - - - - - - - -")
            

account_1 = BankAccount(0.08, 100)
account_2 = BankAccount(0.02, 1000)

account_1.deposit(200), account_1.deposit(50), account_1.deposit(1200),
account_1.withdraw(500),
account_1.yield_interest(),
account_1.display_account_info()

account_2.deposit(1000), account_2.deposit(15000),
account_2.withdraw(500), account_2.withdraw(250), account_2.withdraw(1000), account_2.withdraw(20000)
account_2.yield_interest(),
account_2.display_account_info()