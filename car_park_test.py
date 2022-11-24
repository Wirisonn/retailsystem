from typing import List

car_spaces = [x for x in range(1, 21)]

stats_attributes: list[int] = [0, 0, 0]

# Dictionary with Date as key and a list of parking spaces available
booking_day = {
    1: car_spaces,
    2: car_spaces,
    3: car_spaces,
    4: car_spaces,
    5: car_spaces,
    6: car_spaces,
    7: car_spaces,
    8: car_spaces,
    9: car_spaces,
    10: car_spaces,
    11: car_spaces,
    12: car_spaces,
    13: car_spaces,
    14: car_spaces,
}

stats = {
    1: [0, 0, 0],
    2: [0, 0, 0],
    3: [0, 0, 0],
    4: [0, 0, 0],
    5: [0, 0, 0],
    6: [0, 0, 0],
    7: [0, 0, 0],
    8: [0, 0, 0],
    9: [0, 0, 0],
    10: [0, 0, 0],
    11: [0, 0, 0],
    12: [0, 0, 0],
    13: [0, 0, 0],
    14: [0, 0, 0],
}

# Dictionary to store client information
name_licence = {}

accessible_parking = []
general_parking = []
access_day = []


# Method for Selecting Space for Client
def entry():
    # client booking date
    client_date = int(input("Please Enter Date Between 1-14:\n"))
    # Parking Space Type
    space_type = str(input("Would You Like Accessible or General Parking Space A/G:\n"))
    # Date number validation
    if 0 < client_date < 15:
        # Validating if Date has a free parking space
        if len(booking_day.get(client_date)) > 0:
            # Collecting Client Info
            client_license = str(input('Please Enter License Number:\n'))
            client_name = input('Please Enter Name:\n')
            # Storing Information in a Dictionary
            name_licence.update({str(client_name): str(client_license)})
            # Printing out the Parking Space for the Client

            # For Accessible Parking Space
            if space_type == "A":
                print(client_date)
                print("Your Parking Space Number: ", booking_day.get(client_date)[0])
                # Printing Client Information
                print(name_licence)
                # Removing Booked Space for Client Date
                booking_day.get(client_date).remove(booking_day.get(client_date)[0])
                stats.get(client_date)[0] += 1
                stats.get(client_date)[2] += 1
                print(stats.get(client_date))
                choice = input("Book Date or Look at Statistics B/S:\n")
                if choice == "B":
                    entry()
                elif choice == "S":
                    choose_a_g_t = input("Choose Accessible, General or Total A/G/T:\n")

                    if choose_a_g_t == "A":
                        choose_date = input("Choose Specific Date Between 1-14:\n")
                        print(stats.get(choose_date[0]))
                        print("The number of accessible spaces used on day: ", choose_date, " is: ",
                              stats.get(choose_date)[0])
                        print("The total number of spaces used on day: ", choose_date, " is:",
                              stats.get(choose_date)[2])
                        entry()
                    elif choose_a_g_t == "G":
                        choose_date = input("Choose Specific Date Between 1-14:\n")
                        print("The number of general spaces used on day: ", choose_date, "is: ",
                              stats.get(choose_date)[1])
                        print("The total number of spaces used on day: ", choose_date, " is:",
                              stats.get(choose_date)[2])
                        entry()
                    elif choose_a_g_t == "T":
                        print("The total number of spaces used the whole 14 days is:", len(name_licence))
                        entry()

                    else:
                        print("Please Enter Either A or G or T!!!")
                        entry()


            # For General Parking Space
            elif space_type == "G":
                # Creating list for General Parking Spaces
                g_space = [x for x in booking_day.get(client_date) if x >= 6]
                print("Your Parking Space Number: ", g_space[0])
                # Printing Client Information
                print(name_licence)
                # Removing Booked Space for Client Date
                booking_day.get(client_date).remove(g_space[0])
                stats.get(client_date)[1] += 1
                stats.get(client_date)[2] += 1
                print(stats.get(client_date))
                choice = input("Book Date or Look at Statistics B/S:\n")
                if choice == "B":
                    entry()
                elif choice == "S":
                    choose_a_g_t = input("Choose Accessible, General or Total A/G/T:\n")

                    if choose_a_g_t == "A":
                        choose_date = input("Choose Specific Date Between 1-14:\n")
                        print(stats.get(choose_date[0]))
                        print("The number of accessible spaces used on day: ", choose_date, " is: ",
                              stats.get(choose_date)[0])
                        print("The total number of spaces used on day: ", choose_date, " is:",
                              stats.get(choose_date)[2])
                        entry()
                    elif choose_a_g_t == "G":
                        choose_date = input("Choose Specific Date Between 1-14:\n")
                        print("The number of general spaces used on day: ", choose_date, "is: ",
                              stats.get(choose_date)[1])
                        print("The total number of spaces used on day: ", choose_date, " is:",
                              stats.get(choose_date)[2])
                        entry()
                    elif choose_a_g_t == "T":
                        print("The total number of spaces used the whole 14 days is:", len(name_licence))
                        entry()

                    else:
                        print("Please Enter Either A or G or T!!!")
                        entry()
        else:
            print("Booking is full or select another day")
            entry()
    else:
        print("Please Enter Appropriate Date")
        entry()


entry()
