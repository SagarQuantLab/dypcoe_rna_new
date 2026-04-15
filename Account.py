from Bank import Bank

class Account(Bank):

    def deposit(self, account_number, amount):
        if self.check_existence(account_number):
            self.accounts[account_number]['Balance'] += amount
            return f"Updated balance {self.accounts[account_number]['Balance']}"
        else:
            raise ValueError('Account doesnt exists')

    def withdraw(self, account_number, amount):
        if self.check_existence(account_number):
            current_balance = self.accounts[account_number]['Balance']
            if current_balance >= amount:
                self.accounts[account_number]['Balance'] -= amount
                return f"Updated balance {self.accounts[account_number]['Balance']}"
            else:
                raise ValueError('Insufficient balance') 
        else:
            raise ValueError('Account doesnt exists') 

    def check_balance(self, account_number):
        if self.check_existence(account_number):
            return f"Your account balance {self.accounts[account_number]['Balance']}"
        else:
            raise ValueError('Account doesnt exists')