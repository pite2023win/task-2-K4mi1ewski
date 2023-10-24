

class Client:
    def __init__(self,name="John",cash_amount=0):
        self.name = name
        self.account = cash_amount 
    
    def InputCash(self,cash):
        self.account+=cash

    def WithdrawCash(self,cash):
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