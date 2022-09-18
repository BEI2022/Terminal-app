# import vehicles 
import time, random, p1

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
else:
    # 选择是否是会员
    while True:
        member = input("Are you a member? (yes/no): ")
        if member == "yes":
            p1.member_services()
            break
        elif member == "no":
            sec_member = input("As a member you can enjoy free car wash and free food, there are also discounts on parking fees, do you want to join the membership?: ")
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


# 选择要去的商店
# 输入车牌号
rego = input("Please enter your rego number: ")
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
time_in = time.asctime(time.localtime(time.time()))
print(f"Your check in time is {time_in}")

# check out part
print('--------------------------------------------------------------------------------')
print("Now you're finish shopping and ready to go home -_-")


if date == 1:
    date = int(input("What is today's date?(number only): "))
    print("Today is the monthly membership day with free parking, have a nice day!")
    exit()
elif date != 1:
    
else:
    print("Invalid values please try again.")
