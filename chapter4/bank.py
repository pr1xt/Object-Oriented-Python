class bank():
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance


    def depo(self, ammount):
        print("U will deposit ", ammount," euro")
        self.balance += ammount
        return self.balance


    def disc(self, ammount, password):
        if password != self.password:
            print("Invalid password")
            return None
        elif 0 > ammount or ammount > self.balance:
            print("Incorrect amount to discard")
            return None
        else:
            print("Discarded ", ammount," euro")
            self.balance -= ammount
            return self.balance


    def getBalance(self, password):
        if password == self.password:
            print("Balance is ", self.balance)
            return self.balance


    def show(self):
        print()
        print("name ", self.name)
        print("password ", self.password)
        print("balance ", self.balance)
        return None


acc1 = bank("Alex","qwerty",34)
acc2 = bank("Michel","poiuyt",90)


acc2.depo(43)
acc1.disc(20,"qwerty")

acc1.show()
acc2.show()