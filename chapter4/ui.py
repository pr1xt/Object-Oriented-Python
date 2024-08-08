from controls import manage
oManage = manage()

while True:
    print("*** *** ***")
    print("create acc - 1\ncheck balance - 2\ndeposit - 3\nwithdraw - 4\ndelete acc - 5\nshow all users - 0")

    act = input()
    if act == "1":
       oManage.createAcc()
    elif act == "2":
        oManage.checkBalance()
    elif act == "3":
        oManage.deposit()
    elif act == "4":
        oManage.getMoney()
    elif act == "5":
        oManage.deleteAcc()
    elif act == "0":
        oManage.showAccs()
    else:
        pass

