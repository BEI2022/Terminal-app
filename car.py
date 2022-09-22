import  random, math

from datetime import datetime, timedelta


class Car():
    # time_out
    def __init__(self):
        self.account_money = 50
        # self.time_in = datetime.now()
        # self.time_out = datetime.now()# + timedelta(minutes=3)
        self.rego = int(input("Please enter your rego number: "))

    def start_time(self):
        self.time_in = datetime.now()
        print(f"Your check in time is {self.time_in} ")

    def finish_time(self):
        self.time_out = datetime.now()
        print(f"Your check out time is: {self.time_out}")

    def total_times(self,):
        total_time =  self.time_out - self.time_in
        return total_time

    def check(self):
        print(f"Your account balance is ${self.account_money}")

    def top_up(self,top_up_money):
        print(f"You successfully deposited ${top_up_money}")
        self.account_money = self.account_money + top_up_money
        
    def pay_bill(self, reduce_money):
        print(f"You successfully paid ${reduce_money}")
        x = self.total_times().total_seconds() * 4
        reduce_money = math.floor(x)
        self.account_money = self.account_money - reduce_money


class Temporary():
    def __init__(self,):
        Car.__init__(self,)

    # def run_total_times(self):
    #     self.total_times = Car()
    #     self.total_times.total_times()
       

    def pay_bill(self, x):
        x = math.floor(Car.total_times(self).total_seconds() * 5)
        return x
    


