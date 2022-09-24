from card import Card
import time

class Process:
    def __init__(self):
        self.username_list = [] # store all username
        self.data_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] 
        self.person_list = [] # store total person
        self.account_list = []# store account number
        self.cardlist = []# store card info

    def getusername(self):
        while True:
            name = input("Please enter your username: ")
            if name not in self.username_list:
                return name
            else:
                print("User already exists, please enter your user name again!")

    def getpassword(self):
        while True:
            password = input("please enter your password(3 num):")
            if len(password) == 3:
                for i in range(3):
                    if password[i] not in self.data_list:
                        print("Password must be a number, please enter again!")
                        break
                    if i == 2:
                        return password
            else:
                print("Password must be a number, please enter again!")

    def login(self):    
        while True:
            card_num = input("Please enter your account number: ")
            if card_num in self.account_list:  
                idx = self.account_list.index(card_num) 
                return idx
            else:
                print("This card is not registered, please enter again!")

    def input_pwd(self,card_num):
        idx = self.account_list.index(card_num)
        pwd = input("Please enter your password, you have 3 chances: ")
        num = 2
        while num:
            if pwd == self.cardlist[idx].password:
                return True
            else:
                num -= 1
                pwd = input(f"You have {num + 1} chances for wrong password: ")
                        
    def register(self):
        name = self.getusername()
        card_num = 1000 + len(self.person_list)  
        while str(card_num) in self.account_list:  
            card_num += 1
        card_num = str(card_num)
        pwd = self.getpassword()
        card = Card(card_num, pwd)
        self.account_list.append(card_num)
        self.cardlist.append(card)
        self.username_list.append(name)
        print(f"Registration is successful and the account number is {card_num}")

    def query(self):
        idx = self.login()  
        if True:
            print(f"accont number: {self.cardlist[idx].card_num}, balance: ${self.cardlist[idx].money}")

    def withdraw(self):
        idx = self.login()
        if True:
            while True:
                num = int(input("Please enter the amount to be withdrawn:"))
                if num > self.cardlist[idx].money:
                    print("The amount withdrawn cannot be greater than the account balance!")
                    continue
                else:
                    if self.input_pwd(self.account_list[idx]):   
                        self.cardlist[idx].money -= num
                        print(f"accont number: {self.cardlist[idx].card_num},balance: ${self.cardlist[idx].money}")
                        file = "./transaction.txt"
                        content = time.strftime("%Y-%m-%d %H:%M:%S") + f"## accont number: {self.cardlist[idx].card_num},cash out: ${num},balance: ${self.cardlist[idx].money}\n"
                        with open(file, "a") as f:
                            f.write(content)
                        break
                    else:
                        print("You don't have enough money!")
                        break

    def deposit(self):
        idx = self.login()
        if True:
            while True:
                num = int(input("Please enter the amount to be deposited: "))
                if self.input_pwd(self.account_list[idx]):
                    self.cardlist[idx].money += num
                    print(f"## accont number: {self.cardlist[idx].card_num}, balance: ${self.cardlist[idx].money}")
                    file = "./transaction.txt"
                    content = time.strftime(
                        "%Y-%m-%d %H:%M:%S") + f"## accont number: {self.cardlist[idx].card_num}, deposited ${num}, balance: ${self.cardlist[idx].money}\n"
                    with open(file, "a") as f:
                        f.write(content)
                    break
                else:
                    print("Deposit failed, incorrect password!")
                    break

    def transfer(self):
        idx = self.login()
        if True:
            flag = 1 # 1 = True, 0 = False
            while flag:
                card_num = input("Please enter the transfer account number: ")
                if card_num not in self.account_list:
                    print("Account number does not exist, please enter again!")
                    continue
                else:
                    trfr_idx = self.account_list.index(card_num)
                    while True:
                        num = int(input("Please enter the transfer amount: "))
                        if num > self.cardlist[idx].money:
                            print("The transfer amount cannot be greater than the balance!")
                            continue
                        else:
                            if self.input_pwd(self.account_list[idx]):
                                self.cardlist[idx].money -= num
                                self.cardlist[trfr_idx].money += num
                                print(f"account number: {self.cardlist[idx].card_num}, balance: {self.cardlist[idx].money}")                         
                                flag = 0
                                file = "./transaction.txt"
                                content = time.strftime(
                                    "%Y-%m-%d %H:%M:%S") + f"## account number: {self.cardlist[idx].card_num}, transfer: ${num}, balance: ${self.cardlist[idx].money}\n"
                                with open(file, "a+") as f:
                                    f.write(content)
                                break
                            else:
                                print("Password error, transfer failed!")
                                break