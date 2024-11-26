#create the airplane
class Airplane:
    def __init__(self):
        self._seats = ["Open"] * 20
        self._firstClass = [1,2,3,4,5] #seats in first class
        self._fee = 30.00
        self._emergencyRows =[9,10,15,16]
        self._ticketPrice = 80.00
        self._positionSeat = []

    def availableSeats(self):
        print()
        print(f"This is the seat selection, keep in mind that the first 5 seats are !!First Class!!. \nAnd also Row 5 (seats 9, 10) and Row 8 (seats 15, 16) are in the emergency exit.\n")
        for i in range (len(self._seats)):
            position = i + 1
            self._positionSeat.append(position)
            print(f"Seat {position}: {self._seats[i]}")


    def selectSeat(self):
        tickets = 0
        while tickets != "-1":
            avion.availableSeats()
            tickets = input("According to the seats below select which ones you want to buy (enter -1 to finish)\n")
            if tickets == -1:
                print("Thanks for your visit, goodbye")
            else:
                tickets = tickets.split(',')
                for ticket in tickets:
                    ticket = int(ticket.strip())

                    if ticket in self._positionSeat:
                        pos = self._positionSeat.index(ticket) #pos index number of the seat

                        if self._seats[pos] == "Open":
                            if ticket in self._firstClass:
                                alert = input("This is a first class seat, if you want to enjoy this service theres an extra charge of $30.00\nYou want to continue (yes/no)")
                                if alert.lower() == "yes":
                                    self._seats[pos] = "Occupied"
                                    specialPrice = self._ticketPrice + self._fee
                                    print()
                                    print(f"Seat {ticket} purchased!! the total is: {specialPrice}")
                                else:
                                    print("Ok, you can select another seat")

                            else:
                                if ticket in self._emergencyRows:
                                    alert = input("This is a seat next an emergency row!!!\nIf you want to sit here you have to accept that you would be able to help in case of emergency, select (yes/no)")
                                    if alert.lower() == "yes":
                                        self._seats[pos] = "Occupied"
                                        print()
                                        print(f"Seat {ticket} purchased!! the total is: {self._ticketPrice}")
                                    else:
                                        print("Ok, you can select another seat")
                                else:
                                    self._seats[pos] = "Occupied"
                                    print(f"Seat {ticket} purchased!! the total is: {self._ticketPrice}")
                        else:
                            print("Sorry The seat you selected is already occupied :(\nGo ahead and select another one")
                    else:
                        print("Sorry you have to select a seat between 1 and 20")




avion= Airplane()
avion.availableSeats()
avion.selectSeat()



