from .inventory import Inventory
from .customer import Customer



class Feature:
    def __init__(self):
        self.customer = Customer.customer_info_from_csv()
        self.inventory = Inventory.inventory_info_csv()

    def all_videos(self):
        list_of_videos = []
        for video in self.inventory:
           video_info = {
            "title": video.title,
            "copies_available": video.copies_available
           }
           list_of_videos.append(video_info)
        return list_of_videos

    def all_customers(self):
        customers_dict = {}
        for customer in self.customer:
            customers_dict[customer.id] = {
                "id": customer.id,
                "name": customer.first_name + " " + customer.last_name
        }
        return customers_dict

    def all_of_customer_video_rental(self):
        all_rental = []
        for rent in self.customer:
            customer_rent_info = {
            'current_video_rentals' : rent.current_video_rentals
            }
            without_dash = customer_rent_info['current_video_rentals'].split("/")

            video_rented = {
                'id': rent.id,
                'current_video_rentals': without_dash
            }
            all_rental.append(video_rented)
        return all_rental    

    def add_new_customer(self):
        id = input("Enter customer ID: ")
        account_type = input('nothing:')
        first_name = input("Enter customer first name: ")
        last_name = input("Enter customer last name: ")
        current_video_rentals =input("nothing")
        for customer in self.customer:
            if customer.id == id:
                print("Error: Customer ID already have")
                return
        add_new_customer = Customer(id, account_type, first_name, last_name, current_video_rentals)
        self.customer.append(add_new_customer)
        for i in self.customer:
            print(i.id)

    def renting_video(self, customer_id, title):

        customer = None
        for person in self.customer:
            if int(person.id) == int(customer_id):
                customer = person
                break

        if customer is None:
            print("Error: Customer not found.")
            return

        # Check the rental limit for the customer's account type and current rentals
        if (customer.account_type == 'sx' and len(customer.current_video_rentals) == 1) or \
                (customer.account_type == 'px' and len(customer.current_video_rentals) == 3) or \
                (customer.account_type == 'sf' and ('R' in title or len(customer.current_video_rentals) == 1)) or \
                (customer.account_type == 'pf' and ('R' in title or len(customer.current_video_rentals) == 3)):
            print("Error: Rental limit reached.")
            return

        # Find the video with the matching title
        video = None
        for v in self.inventory:
            if v.title == title:
                video = v
                break

        if video is None:
            print("Error: Video not found.")
            return

        # Check if there are any copies of the video available
        if int(video.copies_available) == 0:
            print("Error: No copies available.")
            return

        # Rent the video
        customer.current_video_rentals += f"/{title}"
        video.copies_available = str(int(video.copies_available) - 1)
        print(f"{title} rented by {customer.first_name} {customer.last_name}")

    def return_video(self, customer_id, title):

        customer = None
        for person in self.customer:
            if int(person.id) == int(customer_id):
                customer = person
                break

        if not customer:
            print(f"Error: Customer {customer_id} not found.")
            return

        if title not in customer.current_video_rentals:
            print(f"Error: Customer {customer_id} hasn't rented video '{title}'.")
            return

        rentals = customer.current_video_rentals.split('/')
        rentals.remove(title)
        customer.current_video_rentals = '/'.join(rentals)

        video = None
        for v in self.inventory:
            if v.title == title:
                video = v
                video.copies_available = str(int(video.copies_available)+1)
                break

        if not video:
            print(f"Error: Video '{title}' not found.")
            return

        print(f"Video '{title}' returned by customer {customer_id}.")

    
    # def all_vid(self):
    #     inventory = Inventory.inventory_info_csv()
    #     Inventory.write_inventory_to_csv(inventory)
    #     for inventor in inventory:
    #         print(inventor.title)
    #         print(inventor.copies_available)


# feature = Feature()
# print(feature.add_new_customer())










