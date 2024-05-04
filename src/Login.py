from src.CustomerLoad import CustomerLoad
from src.Customer import Customer
class LogIn:
    def __init__(self):
        self.email_address = None
        self.customer = None
        
    
    def get_customers(self):
        customer_load = CustomerLoad()
        return customer_load.load_customers()
    

    def log_in(self):
            email_address = input("Enter your email address:")
            customers = self.get_customers()
            for customer in customers:
                if email_address == customer.get_email():
                    if customer.compare_password(input("Enter password: ")):
                        self.email_address = email_address
                        self.customer = customer
                        return True

                    else:
                        print("Wrong password, no second chances")
                        return False
                
            print("Email not found")

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
                
