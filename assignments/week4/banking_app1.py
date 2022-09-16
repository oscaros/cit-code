

class BankAccount:
    def __init__(self, account_number: str, balance: float, owner: str, type: str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
        self.transactions = []

    def __repr__(self) -> str:
        return "Account Number is: {} \nBalance is: {} \nOwner: {} \nAccount Type is: {}".format(self.account_number, self.balance, self.owner, self.type)

    def addtransaction(self, transaction):
        self.transactions.append(transaction)


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
    
    def __repr__(self):
        return "Bank Name is: {}".format(self.name)

    def add_Bank_account(self, bankAct):
        self.accounts.append(bankAct)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []

    def __repr__(self) -> str:
        return "Customer Name is: {}".format(self.name)
    
    def add_bank_account(self, bankAct):
        self.accounts.append(bankAct)

class Transactions:
    def __init__(self, account, amount: float, type: str, previousbalance: float):
        self.account = account
        self.amount = amount
        self.type = type
        self.previousbalance = previousbalance

    def processTransaction(self):
        if self.type == "deposit":
            #newbalance = self.previousbalance + self.amount
            return "Balance after Deposit is: {}".format((float(self.previousbalance + self.amount)))
        
        elif self.type == "withdrawal":
            return "Balance after Withdrawal is: {}".format((float(self.previousbalance - self.amount)))
    

if __name__ == '__main__':
    # while True:
    #     topmenu = int(input("Input 1 to perform a transaction, Input 2 to exit "))

    #     if topmenu == 1:
    #         bankname = input("Enter Bank Name: ")
    #         insidemenu =int(input("Input 1 to open an account, Input 2 to deposit, 3 to withdraw "))

    #         if insidemenu ==1:
    #             customername = input("Enter customer name ")
    #             initialdep = float(input("Enter initial deposit "))
    #             acctno = input("Enter customer name ")
    #             type = input("Enter account type savings or current ")

    #         elif insidemenu == 2:
    #              #get balance before posting transaction
    #             #craete new transaction obj
    #             newTransObject = Transactions("000345556777", 10000, "deposit", newBankAcctObject.balance)
    #             print(newTransObject.processTransaction())

    #         elif insidemenu ==3:
    #              #get balance before posting transaction
    #             #craete new transaction obj
    #             newTransObject = Transactions("000345556777", 10000, "withdrawal", newBankAcctObject.balance)
    #             print(newTransObject.processTransaction())

    #         else:
    #             print("Invalid option")
 
    #     elif topmenu ==2:
    #         break
    #     else:
    #         print("Uknown menu item")
    bankname = input("Enter Bank Name: ")
    customername = input("Enter customer name ")
    initialdep = float(input("Enter initial deposit "))
    acctno = input("Enter account number ")
    type = input("Enter account type savings or current ")

    #create a new bank object
    newbankObject = Bank(bankname)

    #craete a new customer object
    newCustomerObject = Customer(customername)

    #create a new bank account object
    newBankAcctObject = BankAccount(acctno, initialdep, customername, type)

    #print the bank obj
    print(newbankObject)

    #print the cust obj
    print(newCustomerObject)

    #print the bankacct obj
    print(newBankAcctObject)

    insidemenu =int(input("Input 1 to deposit, Input 2 to withdraw "))

    if insidemenu ==1:
        amount =int(input("Input amount to deposit "))
        #get balance before posting transaction
        #craete new transaction obj
        newTransObject = Transactions(acctno, amount, "deposit", newBankAcctObject.balance)
        print(newTransObject.processTransaction())

    elif insidemenu ==2:
        #get balance before posting transaction
        amount =int(input("Input amount to withdraw "))
        #craete new transaction obj
        newTransObject = Transactions(acctno, amount, "withdrawal", newBankAcctObject.balance)
        print(newTransObject.processTransaction())

    else:
        print("invalid output")
    

   



