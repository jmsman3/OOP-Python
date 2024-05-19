#function is a first calss object
def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun
# print(double_decker())
# print(double_decker()())
# print()

def do_somthing(work):
    print( 'Work Started')
    work()
    print('Work End')

# do_somthing(2)
# do_somthing('I am Busy')

def coding():
    print( 'I love coding')

# do_somthing( coding)

def sleeping():
    print( 'I am Not Sleeping')

do_somthing(sleeping)

