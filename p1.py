# class Vehicle:
#     def __init__(self, plate, Identity):
#         self.plate = plate
#         self.Identity = Identity

def member_select():
    member = str(input("Are you a member? (yes/no): "))
    return member

def sec_member_select():
    sec_member = str(input("As a member you can enjoy free car wash and free food, there are also discounts on parking fees, do you want to join the membership?: "))
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


