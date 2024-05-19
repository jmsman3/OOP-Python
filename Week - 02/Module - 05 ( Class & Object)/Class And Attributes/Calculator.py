class calculator:
    brand = 'Casio'
    color_type = 'Black_Light'
    Price = '1200'
    Model = 'Fx_E999_Plus'
    Length = '12 Cm'

    def add(self , num1, num2):
        the_sum = num1 + num2
        add_result = f'Your Sum is {the_sum}'
        return add_result
    
    def Substract(self , num1, num2):
        Subtract = num1 - num2
        Substract_result = f'Your Subtract is {Subtract}'
        return Substract_result
    
    def gun_multipley(self , num1, num2):
        the_gun_multipley= num1 * num2
        gun_multipley_result = f'Your Multiply  is {the_gun_multipley}'
        return  gun_multipley_result
    
    def dividee(self , num1, num2):
        the_dividee= num1 // num2
        dividee_result = f'Your Vaagfol is {the_dividee}'
        return dividee_result
    
my_calculator = calculator()
print ( my_calculator.brand)
print ( my_calculator.color_type)
print ( my_calculator.Price)
print ( my_calculator.Model)
print ( my_calculator.Length)
add_result = my_calculator.add(10 ,3)
print()
print( add_result) #Sum 
print()
Substract_result = my_calculator.Substract(5 ,3)
print( Substract_result) #Deduct
print()
gun_multipley_result = my_calculator.gun_multipley(4,7)
print(gun_multipley_result)
print()  # Multiply 
dividee_result = my_calculator.dividee( 12,2)
print( dividee_result) #Vaag_Korlam



