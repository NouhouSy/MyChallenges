from random import randint as rand

class Account:
    def __init__(self, name, account_number=None, balance = 2000):
        self._name = name
        #when the account number isn't given take a default value
        self._account_number = account_number if account_number is not None else self.generate_account_number()
        self._balance = balance
    #This method help to get the geration the account number
    def generate_account_number(self):
        return rand(1000000000,9999999999)
    #method withdraw
    def withdraw(self, amount):
        try:
            amounts = float(amount)
            if amounts > self._balance:
                print(f"Insufficient funds to withdraw {amount}.\n Current balance: {self._balance}")
            else:
                self._balance-= amounts
                print(f"Withdrew {amount}. \n New balance: {self._balance}") 
        except ValueError:
            print("Please enter a valid balance ): !")
    def deposit(self, amount):
        try:
             amounts = float(amount)
             if amounts<=0:
                print("ERROR:\n Invalid Opration")
             else : 
                 self._balance +=amounts
                 print(f"Deposited {amount}. New balance: {self._balance}")
        except ValueError:
            print("Please enter a valid balance ): !")
    def dump(self):
        print(f"Your account information are:\n Name: {self._name};\n Accounte Number: {self._account_number}; \n Balance: {self._balance} ")


def main():

    # Two account instanciation for Fode Kerfala Camara and Bintou Diaby
    kerfala_account = Account("Fode Kerfala Camara")
    bintou_account = Account("Bintou Diaby")

    # Deposit and withdraw the mony treetimes for kerfala
    kerfala_account.deposit(500)
    kerfala_account.withdraw(1500)
    kerfala_account.withdraw(1000)

    # Deposit and withdraw the mony treetimes for bintou
    bintou_account.deposit(2000)
    bintou_account.withdraw(500)
    bintou_account.deposit(1000)

    # Show informations for the two account
    kerfala_account.dump()
    bintou_account.dump()

if __name__ == '__main__':
    main = main()
    if main:
        print(main)