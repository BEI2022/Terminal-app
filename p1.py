


def menu():
    print("check account balance enter   [1]")
    print("top up enter \t\t[2]")
    print("withdraw money enter\t\t [3]")
    print("transfer money enter\t\t [4]")
    print("back to menuenter \t\t[5]")

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

