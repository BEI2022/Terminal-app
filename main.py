# import vehicles 
import  p1

# chen = vehicles.Vehicle('668-yyl', "member")





# 显示欢迎语
print("Welcome to the Parking System! ")
num = 19 #random.randint(1,20)
print(f"Parking spaces currently available {20 - num}")

# 如果没有位置
if num == 20:
    print("No available parking spaces. If you are a member please go to zone C if not please find another place. ")
    answer = input("Do you wish to continue? (yes/no): ")
    if answer == "yes":
        p1.member_services()
    elif answer == "no":
        exit()
    else:
        print("Invalid values please try again.")
# 如果有空位
else:
    # 选择是否是会员
    while True:
        member = p1.member_select()
        if member == "yes":
            p1.member_services()
            break
        elif member == "no":
            sec_member = p1.sec_member_select()
            if sec_member == "yes":
                print("Welcome! New members! ")
                p1.member_services()
                break
            elif sec_member == "no":
                break
            else:
                print("Invalid values please try again.")
                continue
        else:
            print("Invalid values please try again.")


# 输入车牌号
rego = input("Please enter your rego number: ")

# 选择要去的商店
while True:
    store = int(input("Please choose the store you will visit (1/2): 1. Coles 2. Woolworths: "))
    if store == 1:
        print(f"Please park your car at zone A NO. {num + 1}")
        break
    elif store == 2:
        print(f"Please park your car at zone B NO. {num +1}")
        break
    else:
        print("Invalid values please try again.")

# 记录到访时间
print(f"Your check in time is {p1.start_time()}")

# check out part
print('--------------------------------------------------------------------------------')
print("Now you're finish shopping and ready to go home -_-")

while True:
    temp_out = input("Ready to go home? (yes/no): ")
    if temp_out == "yes":
        print(f"Your check out time is: {p1.finish_time()}")
        # print(f"Your total parking time is: {p1.total_times()}, you need to pay ${p1.total_times * 3}.")
        break
    elif temp_out == "no":
        print("Have fun!")
        # time.sleep(3)
        continue
    else:
        print("Invalid values please try again.")

# 输入车牌以显示车辆停放位置
while True:
    sec_rego = input("Please enter your rego number: ")
    if sec_rego == rego and store == 1:
        print(f"Your vehicles is at zone A NO. {num + 1}")
        break
    elif sec_rego == rego and store == 2:
        print(f"Your vehicles is at zone B NO. {num + 1}")
        break
    else:
        print("Can't find your car please try again.")


# 输入时间以确定是否为免费日
date = int(input("What is today's date?(number only): "))
if date == 1:
    print("Today is the monthly membership day with free parking, have a nice day!")
    exit()
# 非会员结算
elif date != 1 and member == "no" and sec_member == "no":
    while True:
        temp_check_out = input("Do you wish to continue? (y/n): ")
        if temp_check_out == "y":
            while True:
                temp_top_up_money = int(input("Please enter the amount of money you want to top up: "))
                if temp_top_up_money >= {p1.total_times(p1.time_in, p1.time_out) * 3}:
                    print("Thanks for shopping today, have a nice day!")
                    exit()
                elif temp_top_up_money < {p1.total_times(p1.time_in, p1.time_out) * 3}:
                    print("Sorry, your top up money is not enough, please try again.")
                else:
                    print("Invalid values please try again.")
        elif temp_check_out == "no":
            continue
        else:
            print("Invalid values please try again.")

# 会员结算
elif date != 1 and member == "yes" or sec_member == "yes":
    while True:
        member_check_out_option = p1.member_check_out_menu()
        if member_check_out_option == "1":
            p1.member_check()
            continue
        elif member_check_out_option == "2":
            top_up_money = int(input("Please enter the amount you want to top up: "))
            p1.member_top_up(top_up_money)
            continue
        elif member_check_out_option == "3":
            while True:
                saving = p1.member_pay_bill(int(money))
                if saving >= 0:
                    print(f"The payment was successful and your balance is {saving}")
                    print("Thank you for visiting today and see you next time!")
                    exit()
                else: 
                    print("Sorry your balance is not enough please top up")
                    continue
        else:
            print(" Invalid values please try again.")

# 输入错误
else:
    print("Invalid values please try again.")
