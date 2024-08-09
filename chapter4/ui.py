from controls import manage
oManage = manage()

while True:
    print("*** *** ***")
    print("Create acc - 1\nCheck balance - 2\nDeposit - 3\nWithdraw - 4\nDelete acc - 5"
          "\nGet bank info - 9\nShow all users - 0")

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
    elif act == "9":
        oManage.getInfo()
    elif act == "0":
        oManage.showAccs()
    else:
        pass

