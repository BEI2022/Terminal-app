from concurrent.futures import process
from time import *


class Menu:
    def __init__(self):
        self.welcome()
        print("The system is loading, please wait...")
        sleep(1)
        self.operator()

    def welcome(self):
        print("Welcome ZB bank please enter your selection ")

    def operator(self):
        print("------------------------------------------------------------------------------------------------")
        print("[1] Register                  [2] Query")
        print("[3] withdraw                  [4] Deposit")
        print("[5] Transfer                  [0] exit")
        print("------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    process = Menu()