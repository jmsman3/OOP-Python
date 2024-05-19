class Book :
    def __init__(self, cat, id ,name ,quan) -> None:
        self.cat = cat
        self.id = id
        self.name = name 
        self.quan = quan

class User:
    def __init__(self, id, name , password) -> None:
        self.id = id 
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnedBooks = []

class Library:
    def __init__(self, owner , name) -> None:
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
#-------------------------------------------------------------------------------        
    def addBook ( self, cat, id ,name ,quan):
        for book in self.books:
            if book.id == id :
                print(f"This Book id :{book.id} Already added")
                return 
            
        book = Book(cat, id ,name ,quan)
        self.books.append(book)
        print( f'\n\t{book.name} with {book.quan} Pices added Successfully')
#-------------------------------------------------------------------------------
    def addUser(self, id, name , password ):
        for user in self.users:
            if user.id == id :
                print(f"\n\tThis user id: {user.id} Already Exist")
                return 
        user = User(id, name , password)
        self.users.append(user) 
        print(f"\n\tuser id: {user.id},name:{user.name} Registration Done Successfully")
        return user
#-------------------------------------------------------------------------------
    def borrowBook( self, user , id):
        for book in self.books :
            if book.id == id:
                if book in user.borrowedBooks:
                    print(f'\n\tBook id:- {book.id} Already Borrowed')
                    return
                elif book.quan <1:
                    print(f'\n\t Not Available copies')
                    return
                else:
                    user.borrowedBooks.append( book)
                    book.quan = book.quan -1
                    print(f'\n\t Book name {book.name} Borrowed Successfully')
        print(f'\n\t Book Not Found,thanks')
#--------------------------------------------------------------------------------
    def ReturnedBooks( self, user, id):
        for book in self.books:
            if book.id == id :
                if book in user.borrowedBooks:
                    book.quan += 1
                    user.returnedBooks.append(book)
                    user.borrowedBooks.append(book)
                    print(f"\n\t Hey,Return :-{book.name} with id:-{book.id} Successful")
                    return 
                else :
                    print(f"\n\t Hey,You have not finished Reading :-{book.name} with id:-{book.id}")
                    return 
        print(f"\n\t Not Found Any Book,with id:-{book.id}")
                



pl = Library( 'Karim mia' ,'Karim Brothers')
book1 = pl.addBook('Sci_fi', 91,'Intersteler', 6) 
book2 = pl.addBook('Probondhon', 92, 'Sikkha o Monusotto' , 7)
admin = pl.addUser( 'admin' , 'admin' ,'admin')
rahim = pl.addUser('101', 'Md. Rahim' , 'Rahim1234')
sofik = pl.addUser( '102', 'Md. Sofik' , 'Sofik1234')

run = True
currentUser = admin

while True:
    if currentUser == None:
        print(f'\n\t No Logged in User')

        option = input("You want Login or Registration(L/R):-")

        if option == 'R':
            id = int(input("\tEnter id:-"))
            name = input("\tEnter name:-")
            password = input("\tEnter Password:-")

            Registered_user = pl.addUser( id, name , password)
            currentUser = Registered_user


        elif option == "L":
            id = int( input(("\tEnter id:-")))
            password = input("\tEnter Password:-")

            flag_match = False
            for Login_user in pl.users:
                if Login_user.id == id and Login_user.password == password:
                    currentUser = Login_user
                    flag_match = True
                    break 
            if flag_match == False:
                print("\n\tSorry,NO user Found")
    else :
        if currentUser.name == 'admin':
            print("\t========Welcome to Admin Dashboard========\n")
            print("Options:-\n")
            
            print("1 : Add Book")
            print("2 : Show Users")
            print("3 : Show Books")
            print("4 : Logout")

            ch = int(input("\n\tEnter Option:- "))

            if ch == 1:
                cat = input("\tEnter Cat:-")
                id = int( input( "\tEnter id:-"))
                name = input("\tEnter Book Name:-")
                quan = int(input("\tEnter Quan:-"))
                
                pl.addBook(cat, id, name , quan)

            elif ch == 2:
                for Show_user in pl.users:
                    if Show_user.name != 'admin':
                        print(f"Present User name:-{Show_user.name} and id:-{Show_user.id}")
            elif ch == 3:
                for Bok_name in pl.books:
                    print(f"Book name:-{Bok_name.name} and id:-{Bok_name.id} and Quantity:-{Bok_name.quan}")
            elif ch == 4:
                currentUser = None
                print("\n\t Logout Done...!")
        else:
            print("Options:-\n")
            
            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : Show All Book")
            print("4 : Show Borrow Book")
            print("5 : Show History")
            print("6 : Logout")

            ch = int(input("\n\tEnter Option:-"))
            
            if ch == 1:
                id = int(input("\tEnter Book id:-"))
                pl.borrowBook( currentUser, id)

            elif ch == 2:
                id = int(input("\tEnter Book id:-"))
                pl.ReturnedBooks( currentUser, id)
            elif ch == 3:
                print("\n\tShow All Book Below:-\n")

                for all_book in pl.books :
                    if all_book in currentUser.borrowedBooks:
                         print(f'\t Book:- {all_book.name} and id is:- {all_book.id} is Reading Now...!!!')
                    elif all_book in currentUser.returnedBooks:
                         print(f'\t Book:- {all_book.name} and id is:- {all_book.id} is Already Read...!!!')
                    else :
                         print(f'\t Book:- {all_book.name} and id is:- {all_book.id} is Did Not Read...!!!')
            elif ch == 4:
                print("\n\tShow Borrowed Book Below:-")
                for borow_book in currentUser.borrowedBooks:
                    print(f'\t Book:-{borow_book.name} id is:- {borow_book.id} Quantity{borow_book.quan}')
            elif ch == 5:
                print("\n\tShow History Below:-")
                for book in currentUser.returnedBooks:
                    print(f'\t Book:-{book.name} id is:-{book.id} Quantity{book.quan}')
            elif ch == 6:
                currentUser = None
            else :
                print(f"Please Choose valid Options,thank You...!")

                


            


                



            
                    








                    

                


                
       