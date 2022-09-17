# import vehicles 
import time, random

# chen = vehicles.Vehicle('668-yyl', "member")

# 显示欢迎语并输入车牌号码
print("Welcome to the Parking System! ")
num = 20#random.randint(1,20)
print(f"Parking spaces currently available {20 - num}")
rego = input("Please enter your rego number: ")

# 选择要去的商店
store = input("Please choose the store you will visit (1/2): 1. Coles 2. Woolworths: ")

if num == 20:
    print("No available parking spaces.")
elif store == 1 and num != 20:
    print(f"Please park your car at zone A number {num + 1}")
elif store == 2 and num != 20:
    print(f"Please park your car at zone B number {num +1}")
else:
    print("Invalid values")

# 选择是否是会员
while True:
    global member
    member = input("Are you a member? (yes/no): ")
    if member == "yes":
        break
    elif member == "no":
        global sec_member
        sec_member = input("As a member you can enjoy free car wash and free food, do you want to join the membership?: ")
        if sec_member == "yes":
            print("Welcome! New members! ")
            break
        elif sec_member == "no":
            break
        else:
            print("Invalid values")
            continue
    else:
        print("Invalid values")
        
# 记录到访时间
time_in = time.asctime(time.localtime(time.time()))
print(f"Your check in time is {time_in}")


