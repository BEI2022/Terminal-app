# class Vehicle:
#     def __init__(self, plate, Identity):
#         self.plate = plate
#         self.Identity = Identity
import time, datetime

# def member_select():
#     member = input("Are you a member? (yes/no): ")
#     return member

# def sec_member_select():
#     sec_member = input("As a member you can enjoy free car wash and free food, there are also discounts on parking fees, do you want to join the membership?: ")
#     return sec_member

# def member_services():
#     while True:
#         option = int(input("As a member you can choose the following services: 1. free food 2. free car wash 3. other(1/2/3)"))
#         if option == 1:
#             print("Please pick up your food at the front door.")
#             break
#         elif option == 2:
#             print("Please park your car in the car wash area")
#             break
#         elif option == 3:
#             print("Sorry! this option is still under development, please select the other two options.")
#             continue
#         else:
#             print("Invalid values please try again.")

# def time_in():
#     time_in = time.asctime(time.localtime(time.time()))
#     return time_in.


class Time:
    def __init__(self, time, ):
        self.time = time
        # self.finish_time = finish_time
        # self.total_time = total_time

    def start_time(self):
# time_in = time.asctime(time.localtime(time.time()))
        self.start_time = time.ctime()
time_in = Time()
time_in.start_time()
    # return time_in
# timeStruct = time.localtime(time_in)
# strtime = time.strftime("%Y-%m-%d %H:%M:%S",timeStruct)
    # def finish_time(self):
    #     self.finish_time += start_time() 


    # def total_time(self):
        # self.total_time = 

# print(self.start_time())