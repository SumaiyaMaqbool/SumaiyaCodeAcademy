from datetime import date
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = float(balance)
        self.date_of_opening =date_of_opening
        self.customer_name = str(customer_name)
    def deposit(self,new_balance_deposit):
        self.balance+= new_balance_deposit
        return "you despoit {}".format(new_balance_deposit)

    def withdraw (self,new_balance_withdraw):
        self.balance -= new_balance_withdraw
        return "you withrawn {}".format(new_balance_withdraw)
       
    def check_balance(self):
        return "Account Number: {} New balance: {} opening date: {} customer name : {}".format(self.account_number ,self.balance, self.date_of_opening,self.customer_name)

    
cus1=BankAccount(123456789123,5000,"01-01-2023","Jhon")
print(cus1.deposit(100.25))
print(cus1.check_balance())
print(cus1.withdraw(1000.50))

print(cus1.check_balance())








"""print (cus1.customer_order())
print (cus2.customer_order())"""
    