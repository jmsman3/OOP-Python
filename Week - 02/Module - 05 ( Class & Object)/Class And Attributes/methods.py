def call_1(self):
    print('Calling Someone I dont Know')
    return 'Call Done'
class phone:
    price = 12000
    color = 'Blue'
    brand = 'Samsung'
    features = ['Camera', 'Speaker', 'Hammer']

    def call(self):
        print('Calling One Person')
    def send_sms( self, phone , sms):
        text = f'Sending SMS to :  {phone} and Message: {sms}'
        return text
    
my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms( 45454, 'Missi , I missed to Miss You ')
print(result)

