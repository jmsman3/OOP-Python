from ridee import Ride , Ride_request , Ride_matching , RideSharing
from user import Rider, Driver 
from vehicle import Car, Bike

neye_jao = RideSharing("Niye Jao")

rahim = Rider("Rahim mia" , "rahim@gmail.com" , 1234, 1200 , "Mohakhali")
neye_jao.add_rider(rahim)

kolimuddin = Driver("Kolim Uddin" , "kolim@gmail.com" , 343434, "Gulsan")
neye_jao.add_driver(kolimuddin)

rahim.Request_ride( neye_jao , "Uttaara", "car")
kolimuddin.reach_destination(rahim.current_ride)

rahim.Show_current_ride()
