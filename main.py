from Account import Account

accIns = Account()

accIns.open_account(123456789, {'Name':'Rohan', 'Age':35, 'Gender':'Male', 'Balance': 5000})
accIns.open_account(123456788, {'Name':'Sohan', 'Age':25, 'Gender':'Male', 'Balance': 10000})
accIns.open_account(123456787, {'Name':'Mohan', 'Age':25, 'Gender':'Male', 'Balance': 10000})

print(accIns.accounts)
print(accIns.deposit(123456789, 10000))
print(accIns.accounts)
print(accIns.withdraw(123456787, 15000))
