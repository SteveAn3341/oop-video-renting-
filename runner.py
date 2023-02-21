# Write your solution here!

from classes.manage import Feature

code_p_video = Feature()

while True:
    try:
        mode = int(input("""
        == Welcome to Code Platoon Video! ==
        1. View store video inventory
        2. View store customers
        3. View customer rented videos
        4. Add new customer
        5. Rent video
        6. Return video
        7. Exit
        """))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue
    print(mode)

    if mode == 1:
        inventory_list = code_p_video.all_videos()
        for videos in inventory_list:
            print(videos)

    elif mode == 2:
        customers_dict = code_p_video.all_customers()
        for customer_id, customer_info in customers_dict.items():
            print(f"Customer ID: {customer_info['id']}, Name: {customer_info['name']}")


    elif mode == 3:
        rental_list = code_p_video.all_of_customer_video_rental()
        for rental in rental_list:
            print(f"Customer ID: {rental['id']}")
            if rental['current_video_rentals']:
                print("Currently renting:")
                for video in rental['current_video_rentals']:
                    print(f"   - {video}")
            else:
                print("Not currently renting any videos.")

    elif mode == 4:
        code_p_video.add_new_customer()

    elif mode == 5:
        customer_id = input("Enter customer ID: ")
        title = input("Enter video title: ")
        code_p_video.renting_video(int(customer_id), title)

    elif mode == 6:
        customer_id = input("Enter customer ID: ")
        title = input("Enter video title: ")
        code_p_video.return_video(int(customer_id), title)

    elif mode == 7:
        print("Exiting the program...")
        break
    else:
        print("Please enter a valid number.")