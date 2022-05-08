class Atm(object):
    def __init__(self,atmcardnumber,pinnumber):
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
       
    
    def cashWithdrawl(self):
        print("cash has been withdrawled")
        
    def balanceEnquiry(self):
        print("The balance is $100,765")

   

bank=Atm("1689","4586")
print(bank.pinnumber)
bank.cashWithdrawl()