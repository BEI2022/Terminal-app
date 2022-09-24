from card import Card
from person import Person
import time

class Process:
    def __init__(self):
        self.namelist = []
        self.data_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
        self.personlist = []
        self.cardidlist = []
        self.cardlist = []

    def getusername(self):
        while True:
            name = input("Please enter your username: ")
            if name not in self.namelist:
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
            cardid = input("Please enter your account number: ")
            if cardid in self.cardidlist:  
                idx = self.cardidlist.index(cardid)
                return idx
            else:
                print("This card is not registered, please enter again!")

    def input_pwd(self,cardid):
        idx = self.cardidlist.index(cardid)
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
        cardid = 100 + len(self.personlist)  
        while str(cardid) in self.cardidlist:  
            cardid += 1
        cardid = str(cardid)
        pwd = self.getpassword()
        card = Card(cardid, pwd)
        self.cardlist.append(card)
        self.namelist.append(name)
        self.cardidlist.append(cardid)
        print(f"Registration is successful and the card number is{cardid}")

    def query(self):
        idx = self.login()  
        if True:
            print(f"accont number: {self.cardlist[idx].cardid}, balance: ${self.cardlist[idx].money}")

    def withdraw(self):
        idx = self.login()
        if True:
            while True:
                num = int(input("Please enter the amount to be withdrawn:"))
                if num > self.cardlist[idx].money:
                    print("The amount withdrawn cannot be greater than the account balance!")
                    continue
                else:
                    if self.input_pwd(self.cardidlist[idx]):  # check password
                        self.cardlist[idx].money -= num
                        print(f"accont number: {self.cardlist[idx].cardid},balance: ${self.cardlist[idx].money}")
                        file = './transaction.txt'
                        content = time.strftime('%Y-%m-%d %H:%M:%S') + f'##accont number: {self.cardlist[idx].cardid},cash out: {num}元,balance: ${self.cardlist[idx].money}\n'
                        with open(file, 'a') as f:
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
                if self.input_pwd(self.cardidlist[idx]):
                    self.cardlist[idx].money += num
                    print(f"accont number: {self.cardlist[idx].cardid}, balance: ${self.cardlist[idx].money}")
                    file = './transaction.txt'
                    content = time.strftime(
                        '%Y-%m-%d %H:%M:%S') + f'accont number: {self.cardlist[idx].cardid}, deposited ${num}, balance: ${self.cardlist[idx].money}\n'
                    with open(file, 'a') as f:
                        f.write(content)
                    break
                else:
                    print("Deposit failed, incorrect password!")
                    break

    def transfer(self):
        idx = self.login()
        if True:
            flag = 1
            while flag:
                cardid = input("Please enter the transfer account number: ")
                if cardid not in self.cardidlist:
                    print("Account number does not exist, please enter again!")
                    continue
                else:
                    trfr_idx = self.cardidlist.index(cardid)
                    while True:
                        num = int(input("Please enter the transfer amount: "))
                        if num > self.cardlist[idx].money:
                            print("The transfer amount cannot be greater than the balance!")
                            continue
                        else:
                            if self.input_pwd(self.cardidlist[idx]):
                                self.cardlist[idx].money -= num
                                self.cardlist[trfr_idx].money += num
                                print(f"account number: {self.cardlist[idx].cardid}, balance: {self.cardlist[idx].money}")                         
                                flag = 0
                                file = './transaction.txt'
                                content = time.strftime(
                                    '%Y-%m-%d %H:%M:%S') + f'##account number: {self.cardlist[idx].cardid}, transfer: ${num}, balance: {self.cardlist[idx].money}元\n'
                                with open(file, 'a+') as f:
                                    f.write(content)
                                break
                            else:
                                print("Password error, transfer failed!")
                                break