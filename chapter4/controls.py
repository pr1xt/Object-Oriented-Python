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
        print("*** *** ***")
        print("Enter your number")
        inp = input()
        try:
            inp = int(inp.strip())
        except:
            raise AbortTransaction("Invalid account number")
        if str(inp) not in self.accountsDict.keys():
            raise AbortTransaction('There is no account ' + str(inp))
        return str(inp)

    def askForAPassword(self, account):
        print("*** *** ***")
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
        oAcc = self.askForAcc()
        theBalance = oAcc.getBalance()
        print('Your balance is:', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')

    def deposit(self):
        oAcc = self.askForAcc()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAcc.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def getMoney(self):
        oAcc = self.askForAcc()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAcc.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def deleteAcc(self):
        oAcc = self.askForAcc()
        print('Are you sure, that you want to delete your account? Y/N')
        if input().lower()[0] == "y":
            amount = oAcc.getBalance()
            oAcc.withdraw(amount)
            print("Your account will be deleted. Enter your number and password one more time ")
            num = self.askForANum()
            sAcc = self.askForAcc()
            if sAcc == oAcc:
                del self.accountsDict[num]
                print("Take your money: ", amount)
            else:
                raise AbortTransaction("Invalid account")
        elif input().lower()[0] == "n":
            pass


    def showAccs(self):
        print("*** *** ***")
        for i in self.accountsDict.keys():
            print(i)
            self.accountsDict[i].show()
