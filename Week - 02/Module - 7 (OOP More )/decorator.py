import math ,time 
def timer(func):
    def inner( *args , **kargs  ): 
        print('Time Started')    
        start = time.time()
        func(*args , **kargs)
        print('Time Ended')
        end = time.time()
        print( f'Total time is Taken { end - start}')
    return inner
              # *args , **kargs dele (n = 4) airokom parameteer pass kora jai
@timer
def get_factorial(n):
    print('factorial Starting')
    result = math.factorial(n )
    print(f'Factorial of {n} is:- {result}')
get_factorial(n = 4)