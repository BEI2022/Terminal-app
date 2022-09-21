import  random, math

from datetime import datetime, timedelta

class Member():
    # time_out
    def __init__(self):
        self.account_money = 50
        self.time_in = datetime.now()
        self.time_out = datetime.now() + timedelta(minutes=3)
    
    def total_times(self):
        total_time =  self.time_out - self.time_in
        return total_time
        
    def member_check(self):
        print(f"Your account balance is ${self.account_money}")

    def member_top_up(self,top_up_money):
        print(f"You successfully deposited ${top_up_money}")
        self.account_money = self.account_money + top_up_money
        
    def member_pay_bill(self, reduce_money):
        print(f"You successfully paid ${reduce_money}")
        # x = self.total_times().total_seconds() * 2
        # reduce_money = math.floor(x)
        self.account_money = self.account_money - reduce_money