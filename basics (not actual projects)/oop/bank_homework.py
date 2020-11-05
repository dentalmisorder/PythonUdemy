
    #FOR THIS CHALLENGE, CREATE A BANK ACCOUNT CLASS THAT HAS TWO ATTRIBUTES:

    #OWNER
    #BALANCE

    #AND TWO METHODS:

    #DEPOSIT
    #WITHDRAW

class Account():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"""
        ===={self.owner}'s account====
        CARDHOLDER: {self.owner}
        BALANCE: {self.balance}$
        ============================
        """
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}$, now ur balance is {self.balance}$')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Succesfully withdrawn {amount}$ (Balance: {self.balance}$)')
        else:
            print(f'Not enough money! You wanted to withdraw {amount}$, but ur balance is {self.balance}$')
            amount_needed = self.balance - amount
            print(f'If you want to withdraw this amount u need to deposit {abs(amount_needed)}$')

juice_wrld = Account('Juice Wrld', 38000)
iann_dior = Account('iann dior', 23856)

print(juice_wrld)
print(iann_dior)

juice_wrld.withdraw(30156)
juice_wrld.withdraw(8563)

juice_wrld.deposit(800)
juice_wrld.withdraw(8500)