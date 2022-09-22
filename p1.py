


# def member_check_out_menu():
#     print("----------------------------------------------------------------")
#     print("Welcome to the member checkout page, please select the following options.")
#     print("check balance enter   [1]")
#     print("top up enter \t\t[2]")
#     print("pay bill enter\t\t [3]")
#     return input("Please enter your select: ")



def member_select():
    member_select = input("Are you a member? (yes/no): ")
    return member_select


def services():
    while True:
        option = input("As a member you can choose the following services: 1. free food 2. free car wash 3. exit (1/2/3)")
        if option == 1:
            print("Please pick up your food at the front door.")
        elif option == 2:
            print("Please park your car in the car wash area")
        else:
            exit()

