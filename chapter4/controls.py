from bank import bank, AbortTransaction
from accounts import accounts, counter


class manage():

    def __init__(self):
        self.accountsDict = accounts
        self.nextAccountNumber = counter
        self.hours = "9-21/7"
        self.address = "address"
        self.phone = "123456789"

    def askForANum(self):
        print("Enter your number")
        inp = input()
        try:
            inp = int(inp.strip())
        except:
            raise AbortTransaction("Invalid account number")
        if inp not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(inp))
        return inp

    def askForAPassword(self, account):
        print("Enter your password")
        password = input()
        account.checkPassword(password)

    def askForAcc(self):
        num = self.askForANum()
        oAcc = self.accountsDict[num]
        self.askForAPassword(oAcc)
        return oAcc

    def createAcc(self):
        print("*** *** ***")
        print("write down name, deposit, password(divide by space)")
        inp = list(input().split()[:3])
        newAcc = bank(inp[0], inp[1], inp[2])
        self.accountsDict[f"{self.nextAccountNumber}"] = newAcc
        print("your number is ", self.nextAccountNumber)
        self.nextAccountNumber += 1

    def checkBalance(self):
        print("*** *** ***")
        print("write down your number and password")
        inp = list(input().split()[:2])
        print(f"{self.accountsDict[inp[0]].getBalance(inp[1])}")

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')

    def deposit(self):
        print('*** *** ***')
        oAcc = self.askForAcc()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAcc.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def getMoney(self):
        print("*** *** ***")
        oAcc = self.askForAcc()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAcc.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def deleteAcc(self):
        print("*** *** ***")
        print("write down your number and password")
        inp = list(input().split()[:2])
        amount = self.accountsDict[inp[0]].getBalance(inp[1])
        self.accountsDict[inp[0]].withdraw(amount, inp[1])
        del self.accountsDict[inp[0]]
        print("take all your money: ", amount, ".your account has been deleted")

    def showAccs(self):
        print("*** *** ***")
        for i in self.accountsDict.keys():
            self.accountsDict[i].show()
