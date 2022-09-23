class Process:
    def __init__(self):
        self.namelist = []
        self.data_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
        

    def getusername(self):
        while True:
            name = input("Please enter your username: ")
            if name not in self.namelist:
                return name
            else:
                print("用户名已存在，请重新输入用户名!")
                
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