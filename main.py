import time
from menu import Menu
from process import Process
import cowsay



def main():
    menu = Menu()
    process = Process()
    while True:
        num = input("Please enter your selection: ")
        if num == "1":
            process.register()
            time.sleep(1)
            menu.operator()
        elif num == "2":
            process.query()
            time.sleep(1)
            menu.operator()
        elif num == "3":
            process.withdraw()
            time.sleep(1)
            menu.operator()
        elif num == "4":
            process.deposit()
            time.sleep(1)
            menu.operator()
        elif num == "5":
            process.transfer()
            time.sleep(1)
            menu.operator()
        elif num == "0":            
            cowsay.cow("Good bye!")
            exit()
        else:
            print("Invalid input, please try again.")

main()