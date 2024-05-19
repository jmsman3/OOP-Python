from abc import ABC, abstractmethod
from ridee import Ride_matching , RideSharing , Ride_request
class User(ABC):
    def __init__(self, name , email , nid) -> None:
        self.name = name 
        self.email = email 
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError 

class Rider(User):
    def __init__(self, name, email, nid,initial_amount , current_location) -> None:
        super().__init__(name, email, nid)
        self.initial_amount = initial_amount
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider {self.name} and Email {self.email}")
    
    def Load_Cash(self,amount):
        if amount >0:
            self.wallet += amount
        else:
            print(f"Your amount {amount} Less than Zero")

    def Update_location(self,current_location):
        self.current_location = current_location 
    
    def Request_ride(self, ride_sharing , destination, vehicle_type):
        ride_request = Ride_request(self, destination)
        ride_matching = Ride_matching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request , vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("Yay!! we got a ride")
    


    def Show_current_ride(self):
        print("Ride Details!!")
        print(f"Rider : {self.name}")
        print(f"Driver : {self.current_ride.driver.name}")
        print(f"Selected Car : {self.current_ride.vehicle.vehicle_type}")
        print(f"Start Locatrion : {self.current_ride.start_location}")
        print(f"End Locatrion : {self.current_ride.end_location}")
        print(f"Total Cost : {self.current_ride.estimated_fare}")
        

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location 
    
    def display_profile(self):
        print(f"Driver name: {self.name},")
    
    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self) #driver er object
        
    
    def reach_destination(self, ride):
        ride.end_location
    

  



    
        
            


    
















