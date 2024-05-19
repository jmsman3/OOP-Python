class phone:
    manufactured = 'China'
    
    #Constructor
    def __init__(self, owner , brand , price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone , sms):
        text = f'Sending to :{phone} and Sms is :{sms}'
        print(text)

my_phone = phone('Kala Chan', 'Oppo', 9800)
print( my_phone.owner , my_phone.brand , my_phone.price)

her_phone= phone( 'She jann', 'iPhone', 120000)
print(her_phone.owner , her_phone.brand, her_phone.price) 

dad_phone = phone( 'abbu' , 'Nokia' , 3000)
print( dad_phone.owner, dad_phone.brand , dad_phone.price)

