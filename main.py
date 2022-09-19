# import vehicles 
import random, p1,time

# chen = vehicles.Vehicle('668-yyl', "member")

store = None
member = None
sec_member = None
date = None



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
        print(f"Please park your car at zone A number {num + 1}")
        break
    elif store == 2:
        print(f"Please park your car at zone B number {num +1}")
        break
    else:
        print("Invalid values please try again.")

# 记录到访时间
p1.time_in()
print(f"Your check in time is {p1.time_in}")

# check out part
print('--------------------------------------------------------------------------------')
print("Now you're finish shopping and ready to go home -_-")


if date == 1:
    date = int(input("What is today's date?(number only): "))
    print("Today is the monthly membership day with free parking, have a nice day!")
    exit()
elif date != 1 and member == "no" and sec_member == "no":

    while True:
        temp_out = input("Ready to go home? (yes/no): ")
        if temp_out == "yes":
            print(f"Your total parking time is: {time_in}")
            print(f"Your total parking time is: {total_time}, you need to pay ${total_time * 3}.")

            while True:
                temp_check_out = input("Do you wish to continue? (y/n): ")
                if temp_check_out == "y":

                    while True:
                        temp_top_up = int(input("Please enter the amount of money you want to top up: "))
                        if temp_top_up >= {total_time * 3}:
                            print("Thanks for shopping today, have a nice day!")
                            exit()
                        elif temp_top_up < {total_time * 3}:
                            print("Sorry, your top up money is not enough, please try again.")
                        else:
                            print("Invalid values please try again.")

                elif temp_check_out == "no":
                    continue
                else:
                    print("Invalid values please try again.")

        elif temp_out == "no":
            print("Have fun!")
            time.sleep(3)
        else:
            print("Invalid values please try again.")

elif date != 1 and member == "yes" or sec_member == "yes":
    

# else:
#     print("Invalid values please try again.")
