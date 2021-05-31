class ATM(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def CashWithDrawl(self):
        print("WithDrawling Cash")

    def BalanceEnquiry(self):
        print("Your Balance: ")

Bank = ATM(5523674,1256)
Bank.CashWithDrawl()
Bank.BalanceEnquiry()