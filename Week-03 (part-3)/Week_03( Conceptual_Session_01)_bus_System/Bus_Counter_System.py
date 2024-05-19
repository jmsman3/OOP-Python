from abc import ABC, abstractmethod

class AbstractBus(ABC):
    def __init__(self, coach ,driver, arrival , departure, from_des , to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival 
        self.departure = departure
        self.from_des = from_des
        self.to = to 
        # self.seats = ["Empty" for _ in range(20)]
        self.seats = ["0" for _ in range(20)]
class Bus(AbstractBus):
    pass

class BusCompany:
    def __init__(self):
        self.buses = {} #sokol bus er detail thakbe , and database hisebe kaaj korbe 
        #{ 12: bus_object}

    def install_bus(self,bus):
        self.buses[bus.coach] = bus
        print(f"Bus {bus.coach} added successfully")
    
    def display_available_buses(self):
        if not self.buses:
            print("No Bus's are Available")
        else:
            print("coach\tdriver\tarrival\tdprtre\tFromDes\tto")
            for coach ,bus in self.buses.items():
                print(f"{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to}")

    def book_ticket(self,coach, seat):
        if coach in self.buses:
            if 1<=seat<=20 :
                if self.buses[coach].seats[seat-1] == "0":
                    self.buses[coach].seats[seat-1] = "1"
                    print("-----Seat Booking Done-----!!")
                else:
                    print("Seat already booked")
            else:
                print("Invalid Sit Number")
        else:
            print("Invalid Bus Coach Number")

    def Display_seat_Status(self,coach):
        print("======Check Seat status Below=====")
        if coach in self.buses :
            print(self.buses[coach].seats) 


# bus1 = Bus(12, "rahim" , "9.00pm" , "9.30pm","dhaka", "khulna")
# bs = BusCompany()

# bs.install_bus(bus1)
# print(bs.display_available_buses())

company =  BusCompany()
while True:
    print("Welcom to Bus Ticket Booking Sytem....!")
    print("1. install Bus")
    print("2. View Availabe Bus")
    print("3. Book Ticket")
    print("4. Check Seat Status")
    print("5. Exit")
    choice = int(input("Enter Your Choice:-"))
    #  def __init__(self, coach ,driver, arrival , departure, from_des , to):
    if choice == 1:
        coach = int(input("1.Enter Bus Number: "))
        driver = input("2.Enter driver name: ")
        arival = input("2.Enter Arrival Time: ")
        departure = input("4.Enter departure time: ")
        from_dess = input("5.Enter Bus from destination: ")
        to = input("5.Enter Bus destination: ")

        bus = Bus(coach ,driver, arival , departure, from_dess , to)
        company.install_bus(bus)
    elif choice == 2:
        company.display_available_buses()
    
    elif choice == 3:
        coach = int(input("1. Enter coach Number: "))
        seat = int(input("2.Enter Seat Number: "))
        company.book_ticket(coach ,seat)
    elif choice == 4:
        coach = int(input("1.Procide Bus Number: "))
        company.Display_seat_Status(coach)
    elif choice == 5:
        print("Thanks For using our Bus_Ticket_Booking Service")
        break 
    else:
        print("Invalid Choice")


        






    























