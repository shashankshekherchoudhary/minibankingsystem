from random import randint
accounts = []
def generate_account_number():
    while True:
        acc_num = randint(1000, 9999)
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
#View account
def view_account():
    acc_num = int(input("Enter account number to search : "))
    for account in accounts:
        if acc_num == account['acc_num']:
            print("----------------------------------")
            print("        ACCOUNT DETAILS")
            print("----------------------------------")
            print(f"Account Number    : {account['acc_num']}")
            print(f"Account Holder    : {account['name']}")
            print(f"Contact Number    : {account['contact_number']}")
            print(f"Available Balance : ₹{account['balance']}")
            print("----------------------------------")
            break
    else:
        print("❌ Account not found!")

#Deposit money
def deposit_money():
    acc_num = int(input("Enter account number : "))
    for account in accounts:
        if acc_num == account['acc_num']:
            amount = int(input("Enter deposit ammount : "))
            account['balance'] += amount
            print("----------------------------------")
            print("        DEPOSIT SUCCESSFUL")
            print("----------------------------------")
            print(f"Account Number    : {account['acc_num']}")
            print(f"Deposited Amount : ₹{amount}")
            print(f"Updated Balance  : ₹{account['balance']}")
            print("----------------------------------")
            break
    else:
        print("❌ Account not found!")

    