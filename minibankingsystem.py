from random import randint
accounts = []
def generate_account_number():
    while True:
        acc_num = randint(100000, 999999)
        for account in accounts:
            if account["acc_num"] == acc_num:
                break
        else:
            return acc_num

#Create account
def create_account():
    account_number = generate_account_number()
    name = input("Enter account holder name : ")
    minimum_balance = int(input("Deposit minimum balance (Min ₹500) : "))
    contact_number = input("Enter contact number : ")

    account = {
        'acc_num' : account_number ,
        'name' : name ,
        'balance' : minimum_balance ,
        'contact_number' : contact_number
                }
    
    accounts.append(account)


