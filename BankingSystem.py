import os
import random
import datetime


def main():
    balances = {}
    details = {}
    with open('AccountBalances.csv') as f:
        for line in f:
            account, balance = line.split(',')
            balances[account] = int(balance)
    with open('AccountDetails.csv') as f:
        for line in f:
            account, name, address, phone, email = line.split(',')
            details[account] = [name, address, phone, email]
    print("Accounts and Balances")
    for account in balances:
        print(account, balances[account])
    while True:
        print("Banking System")
        print("1. Create Account")
        print("2. Show Account Details")
        print("3. Show Account Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account = random.randint(100000, 999999)
            name = input("Enter your name: ").strip()
            address = input("Enter your address: ").strip()
            phone = input("Enter your phone number: ").strip()
            email = input("Enter your email address: ").strip()
            balances[account] = 0
            details[account] = [name, address, phone, email]
            print("Account created successfully. Your account number is", account)
        elif choice == 2:
            account = (input("Enter your account number: ")).strip()
            if account in details:
                print("Name:", details[account][0])
                print("Address:", details[account][1])
                print("Phone:", details[account][2])
                print("Email:", details[account][3])
            else:
                print("Account not found")
        elif choice == 3:
            account = (input("Enter your account number: ")).strip()
            if account in balances:
                print("Balance:", balances[account])
            else:
                print("Account not found")
        elif choice == 4:
            account = (input("Enter your account number: ")).strip()
            if account in balances:
                amount = int(input("Enter amount to deposit: "))
                balances[account] += amount
                print("Balance:", balances[account])
            else:
                print("Account not found")
        elif choice == 5:
            account = (input("Enter your account number: ")).strip()
            if account in balances:
                amount = int(input("Enter amount to withdraw: "))
                if amount > balances[account]:
                    print("Insufficient balance")
                else:
                    balances[account] -= amount
                    print("Balance:", balances[account])
            else:
                print("Account not found")
        elif choice == 6:
            break
        else:
            print("Invalid choice")
        print()
        with open('AccountBalances.csv', 'w') as f:
            for account in balances:
                f.write(str(account) + ',' + str(balances[account]) + '\n')
        with open('AccountDetails.csv', 'w') as f:
            for account in details:
                line = (str(account) + ',' + details[account][0] + ',' + details[account][1] + ',' + details[account][
                    2] + ',' + details[account][3])
                f.write(line.strip() + '\n')

            os.system('git add .')
            time = datetime.datetime.now()
            os.system('git commit -m "commit at ' + str(time) + '"')


if __name__ == '__main__':
    main()
