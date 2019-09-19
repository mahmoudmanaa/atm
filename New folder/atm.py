class atm :
    def __init__(self,balance,bank_name):
        self.balance= balance
        self.bank_name=bank_name
        self.withdrawals_list = []
    def withdraw (self,request):
        result = self.balance

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdrawals_list.append(request)
            result = self.balance- request

            notes = [100, 50, 10, 5]
            for note in notes:
                while request >= note:
                    request -= note
                    print("give ", str(note))
            if request % 5 != 0:
                print("give",str(request))
                request =0

        return result
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)



balance1 = 500
balance2 = 1000
atm1 = atm(balance1,"smart bank")
atm2 = atm(balance2,"barka")



atm1.withdraw(277)
atm1.withdraw(10)
atm2.withdraw(288)
atm2.withdraw(200)

atm2.show_withdrawals()

