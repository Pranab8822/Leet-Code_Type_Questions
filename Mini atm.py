class ATM:
    
    def __init__(self):
        self.users = {
            "pranab": {"pin": 1234, "balance": 4520.75},
            "neha": {"pin": 4321, "balance": 12000.00},
            "aman": {"pin": 1111, "balance": 305.50},
            "sneha": {"pin": 2222, "balance": 7890.00},
            "raj": {"pin": 3333, "balance": 150.00},
            "ritu": {"pin": 4444, "balance": 99999.99},
            "kumar": {"pin": 5555, "balance": 2500.00},
            "anita": {"pin": 6666, "balance": 640.25},
            "vivek": {"pin": 7777, "balance": 43210.00},
            "sonali": {"pin": 8888, "balance": 0.00} 
        }
    #function for new account creation
    def acc_creation(self,pin,):
        Name=input("Enter your name: ")
        Age=input("Enter your age: ")
        if Age<18:
            print("You are not eligible ")
            exit
        else:
            pin=int(input("Enter 4 digit PIN for you account: "))
            balance=float(input("Enter the balance: "))
        #add info to the dictionary
        self.users[Name] = {"pin": pin, "balance": balance}

    #function for money deposit
    def deposit(self):
        username = input("Enter your username: ")
        pin = int(input("Enter your PIN: "))
        # verify user
        if username in self.users and self.users[username]["pin"] == pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.users[username]["balance"] += amount
            print(f"₹{amount} deposited successfully!")
            print(f"Updated Balance: ₹{self.users[username]['balance']}")
        else:
            print("Invalid username or PIN!")

    #function for money withdrawal
    def Withdraw(self, pin, Amount):
        username = input("Enter your username: ")
        pin=input("Enter the PIN: ")
        if username in self.users and self.users[username]["pin"] == pin:
            Amount=int(input("Enter the amount you want to withdraw: "))
            if Amount > self.users[username]["balance"]:
                print("Insuffecient balance, Please check your account.....")
            elif Amount < self.users[username]["balance"]:
                self.users[username]["balance"] -= Amount
                print(f"{Amount} is successfully debited from you account. ")
                print(f"Updated Balance: ₹{self.users[username]['balance']}")
        else:
            print("PIN not match")        



while True:
    
    print("Welcome to the 'APNA ATM MACHINE' ")
    choice=int(input("Select the process..\n 1.Deposit\n 2.Withdrwal\n 3.Transfer\n 4.Exit\n 5.Create account \n"))
    if choice==1:
        atm = ATM()   
        atm.deposit() 
    elif choice==2:
        atm=ATM()
        atm.Withdraw()
    elif choice==3:
        atm=ATM()
        atm.Transfer()
    elif choice==4:
        exit
    elif choice==5:
        atm=ATM()
        atm.acc_creation()    





