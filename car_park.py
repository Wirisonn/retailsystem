# creating list for the number of parking spaces
car_spaces = [x for x in range(1, 21)]

# creating dictionary to store client information
name_licence = {}
name_date = {}

# list for the dates available
dates = [x for x in range(1, 15)]


# method for booking data entry
def entry():
    # client booking date
    client_date = int(input("Please Enter Date:\n"))

    # condition for completion of booking data entry
    if 0 <= len(name_licence) < 21 and client_date in dates:

        # collecting client data
        client_license = str(input('Please Enter License Number:\n'))
        client_name = input('Please Enter Name:\n')
        name_licence.update({str(client_name): [str(client_license), str(client_date), str(car_spaces[0])]})
        # printing out client information
        print(name_licence)
        # removing booked date
        dates.remove(client_date)
        # removing booked car space
        car_spaces.remove(car_spaces[0])
        entry()

    else:

        print("Sorry Booking is full or Choose another Booking Date")
        if len(car_spaces) == 0 or len:
            dates.extend(range(1, 15))
            name_licence.clear()

        print("Bookings Have Restarted")
        entry()


entry()
print(name_licence)
print(dates)
# for i in range(len(car_spaces)):
