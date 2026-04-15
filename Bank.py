class Bank:

    def __init__(self):
        self.accounts = {}

    # def open_account_decorator(func):
    #     def wrapper(*args):
    #         if not isinstance(args[1], int):
    #             raise ValueError("Account number is not an integer")
    #         return func(*args)
    #     return wrapper

    # @open_account_decorator
    def open_account(self, account_number, account_holder_details):
        """
        Opens account for user
        Parameters:
            account_number: 9 digit number
            account_holder_details: {'Name':'UserName', 'Age':UserAge, 'Gender':'UserGender', 'Balance': UserInitialDeposit}
        Return: String with Account opened details
        """
        if not self.check_existence(account_number):
            self.accounts[account_number] = account_holder_details
            return f"Account created for {account_holder_details['Name']} - {account_number}"
        else:
            raise ValueError(f"Account already exists for {self.accounts[account_number]['Name']}")
    
    def delete_account(self, account_number):
        if self.check_existence(account_number):
            user_name = self.accounts[account_number]['Name']
            self.accounts.pop(account_number)
            return f"Account deleted for - {user_name}"
        else:
            raise ValueError("Account doesn't exists")

    def check_existence(self, account_number):
        account_list = list(self.accounts.keys())
        status = False
        if account_number in account_list:
            status = True
        return status

# bankIns = Bank()
# print(bankIns.open_account(123456789, {'Name':'Rohan', 'Age':35, 'Gender':'Male', 'Balance': 5000}))
# print(bankIns.open_account(123456788, {'Name':'Sohan', 'Age':25, 'Gender':'Male', 'Balance': 10000}))
# print(bankIns.open_account(123456787, {'Name':'Mohan', 'Age':25, 'Gender':'Male', 'Balance': 10000}))
# print(bankIns.accounts)
# print(bankIns.delete_account(123456787))
# print(bankIns.accounts)
# print(bankIns.delete_account(123456780))