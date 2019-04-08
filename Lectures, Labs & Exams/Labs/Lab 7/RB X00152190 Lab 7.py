class hotelRoom:
    roomNumber = 0
    maxGuests = 0
    numGuests = 0
    nightsBooked = 0
    roomInUse = False

    # static variables
    countRoomsInUse = 0
    countTotalGuests = 0
    peekSeason = True

    def __init__(self, roomNumber_in=0, maxGuests_in=0):
        self.numGuests = 0
        self.nightsBooked = 0
        self.roomInUse = 0
        self.roomNumber = roomNumber_in
        self.maxGuests = maxGuests_in



    # static method - don't need self here
    @staticmethod
    def Cost_room():
        nightStayCost = 0
        if hotelRoom.peekSeason: # static variable
            nightStayCost += 250
        else:
            nightStayCost += 150
        return nightStayCost


    def check_in(self, numGuests_in=0, nightsBooked_in=0, roomInUse_in=True ):
        self.roomInUse = roomInUse_in
        self.numGuests = numGuests_in
        self.nightsBooked = nightsBooked_in
        hotelRoom.countRoomsInUse += 1
        hotelRoom.countTotalGuests += self.numGuests




    # # static method - don't need self here
    # @staticmethod
    def check_out(self):
        self.numGuests = 0
        self.nightsBooked = 0
        self.roomInUse = False
        hotelRoom.countRoomsInUse -= 1
        hotelRoom.countTotalGuests = 0


    # Dont actually need this but in case we did what a print def within our class
    # def my_print(self):
    #     print('*****************')
    #     print('** Hotel Costs **')
    #     print('Total Guests: {}'.format(hotelRoom.countTotalGuests))
    #     print('Total Rooms in Use: {}'.format(hotelRoom.countRoomsInUse))
    #     if hotelRoom.peekSeason:
    #         print("Peek Season: Yes")
    #     else:
    #         print("Peek Season: No")
    #     #print('Room Cost: {}'.format()) # how to call return functions
    #     print('Room Number: {}'.format(self.roomNumber))
    #     print('Max Guests: {}'.format(self.maxGuests))
    #     print('Number of Guests: {}'.format(self.numGuests))
    #     print('Nights Booked: {}'.format(self.nightsBooked))
    #     print('Room In Use: {}'.format(self.roomInUse))


#class instance

# Test this class in the main program body using the following:

# • Create two rooms with appropriate arguments
room1 = hotelRoom(5,8) # init arguments
room2 = hotelRoom(10,12) # init arguments


# • Print the static variables to show total guests in hotel and total rooms in use
print('Rooms in Use Pre Check In: {}'.format(hotelRoom.countRoomsInUse)) # 0
print('Total Guests Pre Check In: {}'.format(hotelRoom.countTotalGuests)) # 0
print('Peek Season: {}\n'.format(hotelRoom.peekSeason)) # True

# • Check in guests to both rooms using appropriate arguments
room1.check_in(2,10) # didn't need to pass in room in use as set to True
room2.check_in(5,20) # didn't need to pass in room in use as set to True

# • Print the cost of each room
print("Room 1 Cost: €{}".format(int(room1.Cost_room()) * (room1.nightsBooked)))
print("Room 2 Cost: €{}\n".format(int(room2.Cost_room()) *(room2.nightsBooked)))

# • Print the static variables to show total guests in hotel and total rooms in use
print('Rooms in Use Post Check In: {}'.format(hotelRoom.countRoomsInUse)) # 0 # **** check how I got that right *****
print('Total Guests Post Check In: {}\n'.format(hotelRoom.countTotalGuests)) # 0

# Don't need this just had if want to print like this - room1.my_print()

# • Check out guests from both rooms
room1.check_out()
room2.check_out()

# • Print the static variables to show total guests in hotel and total rooms in use
print('Rooms in Use Post Check Out: {}'.format(hotelRoom.countRoomsInUse)) # 0 # **** check how I got that right *****
print('Total Guests Post Check Out: {}\n'.format(hotelRoom.countTotalGuests)) # 0








