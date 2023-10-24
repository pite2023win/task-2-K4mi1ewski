#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Client:
    def __init__(self,name="John",cash_amount=0):
        self.name = name
        self.account = cash_amount 
    
    def input_cash(self,cash):
        self.account+=cash

    def withdraw_cash(self,cash):
        self.account-=cash


class Bank:   
    def __init__(self):
        print("Creating a new bank.")
        self.clients=[]
    
    def AddClient(client):
        self.clients.append(client)

    def TransferMoney(client_from, client_to, money):
        pass




if __name__ == "__main__":
    print("Starting simulation.")

    try:
        bank=Bank()
        while True:
            print("If you want to add a new client, press 1.")
            print("If you want to transfer money from one client to another, press 2.")
            choice = int(input())
            if choice != 1 and choice !=2:
                print("Wrong input, try once more")
            else:
                if choice == 1:
                    client_name=input("New client's name:")
                    clients_cash=int(input("New client's account value:"))
                    new_client=Client(client_name,clients_cash)
                    bank.AddClient(new_client)
                if choice == 2:
                    client_transferer_name=input("Name of the client, from whom you want to tranfer money")
                    client_receiver_name=input("Name of the client, to whom you want to transfer money")
                    cash_amonut=int(input("Amount of the cash you want to transfer"))
            


    except KeyboardInterrupt:
        print("End of simulation.")