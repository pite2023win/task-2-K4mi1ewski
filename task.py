import multiprocessing
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Client:
    total_clients_count = 0
    
    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance
        self.account_number = Client.total_clients_count
        Client.total_clients_count += 1
        
    @staticmethod
    def deposit(client, amount):
        client.balance += amount
        logger.info("Client {} deposited {}$.".format(client.name, amount))

    @staticmethod
    def withdraw(client, amount):
        if client.balance >= amount:
            client.balance -= amount
            logger.info("Client {} withdrew {}$.".format(client.name, amount))
        else:
            logger.info("Insufficient balance!")
            
    @staticmethod
    def transfer(sender, receiver, amount):
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            logger.info()
        else:
            logger.info("Insufficient balance!")      
   
    @staticmethod
    def client_info(client):
        return f"Account Number: {client.account_number}, Name: {client.name}, Balance: {client.balance}"
         
            
class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def save_bank_data(self, file_name):
        with open(file_name, 'w') as file:
            file.write("Bank name: {}\n".format(self.name))
            file.write("Clients:\n")
            for client in self.clients:
                file.write("Name: {}; Account number: {}; Balance: {}\n".format(client.name, client.account_number, client.balance))

    def add_client(self, client):
        self.clients.append(client)
        logger.info("Client {} has been added to the bank: {}".format(client.name, self.name))
    
    def delete_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            logger.info("Client {} has been removed from the {} bank!".format(client.name, self.name))
        else:
            logger.info("Client {} not found in the {} bank!".format(client.name, self.name))    
            
    def read_bank_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                client_data = []
                current_client = None

                for line in lines:
                    line = line.strip()
                    if line.startswith("Bank Name:"):
                        self.name = line.split("Bank Name:")[1].strip()
                    elif line == "Clients:":
                        current_client = {}
                    elif line.startswith("Account Number:"):
                        account_number = int(line.split("Account Number:")[1].strip())
                        current_client["Account Number"] = account_number
                    elif line.startswith("Name:"):
                        name = line.split("Name:")[1].strip()
                        current_client["Name"] = name
                    elif line.startswith("Balance:"):
                        balance = int(line.split("Balance:")[1].strip())
                        current_client["Balance"] = balance
                        self.clients.append(Client(current_client["Name"], current_client["Balance"]))

        except FileNotFoundError:
            logging.error("File '{}' not found.".format(file_name))


if __name__ == "__main__":
    bank_1 = Bank("First Bank")
    bank_2 = Bank("Second Bank")
    bank_3 = Bank("Third Bank")
    
    client_1 = Client("Bob")
    client_2 = Client("George", 600)
    client_3 = Client("Chris", 2500)
    client_4 = Client("Alex", 4000)
    client_5 = Client("Arthur", 100)
    
    bank_1.add_client(client_1)
    bank_1.add_client(client_2)
    
    bank_2.add_client(client_3)
    
    bank_3.add_client(client_4)
    bank_3.add_client(client_5)
    
    print("List of clients in the {}:".format(bank_1.name))
    for client in bank_1.clients:
        print(Client.client_info(client))
    
    print("List of clients in the {}:".format(bank_2.name))
    for client in bank_2.clients:
        print(Client.client_info(client))
        
    print("List of clients in the {}:".format(bank_3.name))
    for client in bank_3.clients:
        print(Client.client_info(client))    
    
    bank_1.delete_client(client_2)
    
    print("List of clients in the {}:".format(bank_1.name))
    for client in bank_1.clients:
        print(Client.client_info(client))
    
    Client.deposit(client_3, 500)
    Client.withdraw(client_5, 1000)
    Client.withdraw(client_3, 1000)
    Client.withdraw(client_1, 100)
    Client.deposit(client_5, 400)
    Client.deposit(client_2, 300)
    
    bank_2.add_client(client_2)
    
    print("List of clients in the {}:".format(bank_1.name))
    for client in bank_1.clients:
        print(Client.client_info(client))
    
    print("List of clients in the {}:".format(bank_2.name))
    for client in bank_2.clients:
        print(Client.client_info(client))
        
    print("List of clients in the {}:".format(bank_3.name))
    for client in bank_3.clients:
        print(Client.client_info(client))
     
    bank_1.save_bank_data("bank_1_info.txt")
     
    bank_1_copy = Bank ("first bank copy")
    bank_1_copy.read_bank_data("bank_1_info.txt")
    
    print("List of clients in the {}:".format(bank_1_copy.name))
    for client in bank_1_copy.clients:
        print(Client.client_info(client)) 
        
    with multiprocessing.Pool(processes=2) as pool:
        pool.apply_async(Client.deposit, (client_1, 100))
        pool.apply_async(Client.deposit, (client_2, 50))
        pool.close()
        pool.join()
        