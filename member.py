import  random, math

from datetime import datetime, timedelta


class Member():
    # # time_out
    def __init__(self, account, ):
        self.account = account
        self.account_money = 300
    
        

    # def start_time(self):
    #     self.time_in = datetime.now()
    #     print(f"Your check in time is {self.time_in} ")
    #     # return self.time_in

    # def finish_time(self):
    #     self.time_out = datetime.now()
    #     print(f"Your check out time is: {self.time_out}")
    #     # return self.time_out

    # def total_times(self,):
    #     self.total_time =  self.time_out - self.time_in
    #     return self.total_time

    def check(self):
        print(f"Your account balance is ${self.account_money}")

    def to_up(self,top_up_money):
        print(f"You successfully deposited ${top_up_money}")
        self.account_money = self.account_money + top_up_money
        
    def pay_bill(self, reduce_money):
        print(f"You successfully paid ${reduce_money}")
        # x = self.total_times().total_seconds() * 4
        # reduce_money = math.floor(x)
        self.account_money = self.account_money - reduce_money





