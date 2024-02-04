class Bank:
    def __init__(self,owner, balance=0, deposit1=0):
        self.owner=owner
        self.balance=balance
        self.deposit1=deposit1
    def withdrawn(self, summa):
        if summa>0:
            if summa <= self.balance:
                self.balance -= summa

                print(f"Withdrawn: {summa}.\nNew balance: {self.balance}")
            else:
                print("Not enough funds to withdrawn")
        else:
            print("Wrong withdrawal amount")
    def deposit(self, summa1):
        if summa1 > 0:
            if summa1 <= self.balance:
                self.balance -= summa1
                self.deposit1 += summa1
                print(f"Deposit: {self.deposit1}.\nNew balance: {self.balance}")
            else:
                print("Not enough funds to deposite")
        else:
            print("Wrong withdrawal amount")


#Bank class
bank = Bank("Sadyk Akzhol", 9999, 1000)

#Test
print(f"Account: {bank.owner}")
print(f"Balance: {bank.balance}")
bank.withdrawn(5000)
bank.deposit(4000)
print(f"Final Balance: {bank.balance} and in deposit: {bank.deposit1}")

    
    