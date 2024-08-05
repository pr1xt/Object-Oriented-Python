from bank import bank
from accounts import accounts,counter

while True:
    print("create acc - 1\ncheck balance - 2\ndeposit - 3\nwithdraw - 4\nshow all users - 0")

    act = input()[0]
    if act == "1":
        print("write down name, deposit, password(divide by space)")
        inp = list(input().split()[:3])
        bank(inp[0],inp[1],inp[2])
        print("your number is ", counter)
        counter += 1
    elif act == "2":
        print("write down your number and password")
        inp = list(input().split()[:2])
        print(f"{accounts[inp[0]].getBalance(inp[1])}")
    elif act == "3":
        print("write down your number, amount to deposit and password")
        inp = list(input().split()[:3])
        print(f"{accounts[inp[0]].deposit(int(inp[1]),inp[2])}")
    elif act == "4":
        print("write down your number, amount to withdraw and password")
        inp = list(input().split()[:3])
        print(f"{accounts[inp[0]].withdraw(int(inp[1]), inp[2])}")
    elif act == "0":
        for i in accounts.keys():
            accounts[i].show()

