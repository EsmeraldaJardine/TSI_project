from ReadCSVFile import ReadCSVFile
from Customer import Customer

class CustomerLoad:

    def get_raw_customer(self):
        read_csv_file = ReadCSVFile()
        customer_data = read_csv_file.get_file_data("customer.csv")
        return customer_data

    def load_customers(self):
        customers = []
        raw_customer_data = self.get_raw_customer()
        for customer in raw_customer_data:
            customers.append(Customer(customer))
        return customers

    def format_customers(self):
        display = ""
        customers = self.load_customers()
        for customer in customers:
            display += customer.get_name() + "\n"
        return display
    
    def get_customer(self, email):
        customers = self.load_customers()
        for customer in customers:
            if email == customer.get_email():
                return customer
        return None

if __name__ == '__main__':
    customer_load = CustomerLoad()
    print(customer_load.format_customers())
