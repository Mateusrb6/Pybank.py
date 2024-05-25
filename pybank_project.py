class BankAccount:
    def __init__(self, first_name, last_name, account_id, pin, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.pin = pin
        self.balance = balance

    def deposit(self):
        money_added = float(input('deposit = '))
        if money_added < 0:
            print('deposit amount must be positive.')
            return
        
        self.balance += money_added
        print(f'Now you have {self.balance} dolars.')
    
    def withdraw(self):
        money_withdraw = float(input('withdraw = '))
        if money_withdraw <= self.balance:
            self.balance -= money_withdraw
            print(f'the withdraw was {money_withdraw} dolars.\n')
            print(f'Now you have {self.balance} dolars.')

        elif money_withdraw < 0:
            print('withdraw amount must be positive')
            return
        
        else:
            print('insufficient funds.')

    def display_balance(self):
        print(f'You have {self.balance} dolars.')

    def display_welcome(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}, Welcome to PyBank!\n')

def beginning():
    print('\t==============')
    print('\t   PYBANK')
    print('\t==============')

def enter(accounts):
    print('Do you want to register? (YES/NO)')
    
    answer = str(input('').strip().upper())

    if answer == 'YES':
        first_name = str(input("Enter your first name: "))
        last_name = str(input("Enter your last name: "))

        print('\n')

        account_id = int(input("Enter your account ID: "))
        account_pin = int(input("Enter your account PIN: "))

        if len(str(account_pin)) < 6:
            print('password is too short. Try another.')
            account_pin = int(input("Enter your account PIN: "))

        print('\n')

        account = BankAccount(first_name, last_name, account_id, account_pin)
        account.display_welcome()
        return account
    else:
        print('Exiting...')
        return None

def menu_options(account):
    while True:
        print('\t--Options Menu--\n1) Deposit\n2) Withdraw\n3) Display balance\n4) Exit\n')
        options = int(input('').strip())

        if options == 1:
            account.deposit()
        elif options == 2:    
            account.withdraw()
        elif options == 3:
            account.display_balance()
        elif options == 4:
            print('exiting...')
            return False
        else:
            print('invalid option.')
       

accounts = []

beginning()

while True:
    account = enter(accounts)
    if account:
        accounts.append(account)
        if not menu_options(account):
            break
    else:
        break


