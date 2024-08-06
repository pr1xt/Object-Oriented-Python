from bank import bank
from accounts import accounts,counter

class manage():

    def __init__(self):
        self.accountsDict = accounts
        self.nextAccountNumber = counter

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

    def deposit(self):
        print("*** *** ***")
        print("write down your number, amount to deposit and password")
        inp = list(input().split()[:3])
        print(f"{self.accountsDict[inp[0]].deposit(int(inp[1]), inp[2])}")

    def getMoney(self):
        print("*** *** ***")
        print("write down your number, amount to withdraw and password")
        inp = list(input().split()[:3])
        print(f"{self.accountsDict[inp[0]].withdraw(int(inp[1]), inp[2])}")

    def deleteAcc(self):
        print("*** *** ***")
        print("write down your number and password")
        inp = list(input().split()[:2])
        amount = self.accountsDict[inp[0]].getBalance(inp[1])
        self.accountsDict[inp[0]].withdraw(amount, inp[1])
        del self.accountsDict[inp[0]]
        print("take all your money: ", amount,".your account has been deleted")

    def showAccs(self):
        print("*** *** ***")
        for i in self.accountsDict.keys():
            self.accountsDict[i].show()