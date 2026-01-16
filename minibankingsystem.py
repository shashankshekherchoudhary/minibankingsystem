from random import randint
accounts = []
def generate_account_number():
    while True:
        acc_no = randint(100000, 999999)
        for account in accounts:
            if account["acc_no"] == acc_no:
                break
        else:
            return acc_no
