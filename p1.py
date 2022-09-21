# class Vehicle:
#     def __init__(self, plate, Identity):
#         self.plate = plate
#         self.Identity = Identity



# def member_check_out_menu():
#     print("----------------------------------------------------------------")
#     print("Welcome to the member checkout page, please select the following options.")
#     print("check balance enter   [1]")
#     print("top up enter \t\t[2]")
#     print("pay bill enter\t\t [3]")
#     return input("Please enter your select: ")





# store = None
# member = None
# sec_member = None
# date = None
# account_money = random.randint(0,30)

def member_select():
    member = input("Are you a member? (yes/no): ")
    return member

def sec_member_select():
    sec_member = input("As a member you can enjoy free car wash and free food, there are also discounts on parking fees, do you want to join the membership?: ")
    return sec_member

def member_services():
    while True:
        option = int(input("As a member you can choose the following services: 1. free food 2. free car wash 3. other(1/2/3)"))
        if option == 1:
            print("Please pick up your food at the front door.")
            break
        elif option == 2:
            print("Please park your car in the car wash area")
            break
        elif option == 3:
            print("Sorry! this option is still under development, please select the other two options.")
            continue
        else:
            print("Invalid values please try again.")

def start_time():
    pass
    # time_in = 
    # return time_in

def finish_time():
    # time.sleep(3)
    time_out = datetime.now()
    return time_out
# time_in = start_time()
# time_out = finish_time()





# def total_times():
#     total_time =  exit_time - entry_time
#     return total_time
