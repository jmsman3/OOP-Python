balance = 3000

def buy_things( item, price):

    #  local scope variable
    #  you can use globale variable without using global keyword
    # if you want to modify global variable you have to use global keyword
    global balance
    print( 'Previous balance value: ', balance)
    balance = balance - price
    print('balance after buying:', balance)

buy_things( 'Sungalss', 1000)

# print( 'globgal balance after buy', balance)
    