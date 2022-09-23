from member import Member


def top():
    print("----------------------------------------------------------------")
    print("Welcome to the member checkout page, please select the following options.")
    print("check balance enter   [1]")
    print("top up enter   [2]")
    print("pay bill enter [3]")
def main(): 
    while True :
        x = input("Please enter your select: ")
        if x == "1":
            Member.check()
        elif x == "2":
            y = int(input("Please enter the amount you want to top up: "))
            member.to_up(y)
        elif x == "3":
            member.pay_bill(z)
            member.check()
        else:
            break

top()
main()

