
import p1
from car import Car
from car import Temporary 








temp = Temporary()
# 显示欢迎语
print("Welcome to the Parking System! ")
num = 19 #random.randint(1,20)
print(f"Parking spaces currently available {20 - num}")

# 如果没有位置
# if num == 20:
#     print("No available parking spaces. If you are a member please go to zone C if not please find another place. ")
#     answer = input("Do you wish to continue? (yes/no): ")
#     if answer == "yes":
#         p1.services()
#     elif answer == "no":
#         exit()
#     else:
#         print("Invalid values please try again.")
# # 如果有空位
# else:
#     # 选择是否是会员
#     while True:
#         member_select = input("Are you a member? (yes/no): ")
#         if member_select == "yes":
#                p1.services()
            
#         elif member_select == "no":
#             sec_member = input("As a member you can enjoy free car wash and free food, there are also discounts on parking fees, do you want to join the membership?: ")
#             if sec_member == "yes":
#                 print("Welcome! New members! ")
#                 p1.services()
#             else:
#                 print("Invalid values please try again.")
#         else:
#             print("Invalid values please try again.")

# 输入车牌号
car = Car()
# car.rego 
# 记录到访时间
# print(f"Your check in time is {car.time_in} ")
car.start_time()

# check out part
print('--------------------------------------------------------------------------------')
print("Now you're finish shopping and ready to go home -_-")

while True:
    temp_out = input("Ready to go home? (yes/no): ")
    if temp_out == "yes":
        # print(f"Your check out time is: {car.time_out}")
        car.finish_time()
        # print(f"Your total parking time is: {car.total_time}, you need to pay ${temp.pay_bill(10)}.")
        break
    elif temp_out == "no":
        print("Have fun!")
        # time.sleep(3)
        continue
    else:
        print("Invalid values please try again.")

# 输入车牌以显示车辆停放位置
# while True:
#     sec_rego = input("Please enter your rego number: ")
#     if sec_rego == rego and store == 1:
#         print(f"Your vehicles is at zone A NO. {num + 1}")
#         break
#     elif sec_rego == rego and store == 2:
#         print(f"Your vehicles is at zone B NO. {num + 1}")
#         break
#     else:
#         print("Can't find your car please try again.")

# 非会员结算
if p1.member_select() == "no" :
    while True:
        temp_check_out = input("Do you wish to continue? (y/n): ")
        if temp_check_out == "y":
            print(f"Your parking time is {car.total_times()}, you need to pay {temp.pay_bill(10)}")
            while True:
                temp_top_up_money = int(input("Please enter the amount of money you want to top up: "))
                if temp_top_up_money >= {temp.pay_bill(10)}:
                    print("Thanks for shopping today, have a nice day!")
                    exit()
                elif temp_top_up_money < {temp.pay_bill(10)}:
                    print("Sorry, your top up money is not enough, please try again.")
                else:
                    print("Invalid values please try again.")
        elif temp_check_out == "no":
            continue
        else:
            print("Invalid values please try again.")

# 会员结算
elif p1.member_select() == "yes" :
    print("----------------------------------------------------------------")
    print("Welcome to the member checkout page, please select the following options.")
    print("check balance enter   [1]")
    print("top up enter   [2]")
    print("pay bill enter [3]")
    
    while True :
        x = input("Please enter your select: ")
        if x == "1":
            car.check()
        elif x == "2":
            car.top_up(10)
        elif x == "3":
            car.pay_bill(10)
            car.check()
        else:
            continue
