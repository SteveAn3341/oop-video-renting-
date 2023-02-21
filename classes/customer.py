import csv

class Customer:

    def __init__(self, id, account_type, first_name, last_name, current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        self.name = first_name + " " + last_name

    def customer_info_from_csv():

        customer_list = []
        with open('data/customers.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                customer_list.append(Customer(**row))
        return customer_list   

# customers = Customer.customer_info_from_csv()
# for customer in customers:
#     print(customer.first_name + " " + customer.last_name)
#     print(customer.current_video_rentals)


