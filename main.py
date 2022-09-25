from time import *
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
            sleep(1)
            menu.operator()
        elif num == "2":
            process.query()
            sleep(1)
            menu.operator()
        elif num == "3":
            process.withdraw()
            sleep(1)
            menu.operator()
        elif num == "4":
            process.deposit()
            sleep(1)
            menu.operator()
        elif num == "5":
            process.transfer()
            sleep(1)
            menu.operator()
        elif num == "0":            
            cowsay.cow("Good bye!")
            exit()
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
