from src.CustomerLoad import CustomerLoad
from src.Customer import Customer
class LogIn:
    def __init__(self):
        self.email_address = None
        self.customer = None
        
    def get_password(self,email_address):
        customerLoad = CustomerLoad()
        customers = customerLoad.load_customers()
        password = ""
        counter = 0
        while password == "" and counter < len(customers):
            if email_address == customers[counter].get_email():
                password = customers[counter].password
                self.customer = customers[counter]
            counter += 1
        return password

    def log_in(self):
            email_address = input("Enter your email address:")
            password = self.get_password(email_address)
            if password == "":
                print("You are not a user")
                return False

            if input("Enter password: ") == password:
                self.email_address = email_address
                return True
            else:
                print("Wrong password, no second chances")
                return False

    def get_customer_attributes(self):
        if self.customer is None:
            return None

        return {
            'email': self.customer.get_email(),
            'first_name': self.customer.get_first_name(),
            'last_name': self.customer.get_last_name(),
            'total_wins': self.customer.get_total_games_won(),
            'total_losses': self.customer.get_total_games_lost(),
        }
                
