class Star_cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_cinema.__hall_list.append(hall)


class Hall(Star_cinema):

    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}      #protected property
        self._show_list = []  #protected property
        self._rows = rows     #protected property
        self._cols = cols     #protected property
        self.hall_no = hall_no
        self.entry_hall()

    def entry_hall(self, hall = None):
        super().entry_hall(hall)
# ------------------------------------------------------------------------------
    def entry_show(self, id, movie_name, time):
        show_tuple = (id, movie_name, time)
        self._show_list.append(show_tuple)
        self._seats[id] = [[0, 0, 0, 0, 0] for _ in range(self._rows)]
#------------------------------------------------------------------------------
    def Book_Seats(self, id, seat_wanna_book):
        if id not in self._seats:
             print(f' Show id-{id} is Invalid..!')
             return
           
        for row, col in seat_wanna_book:
            if 0 <= row < self._rows and 0 <= col < self._cols:
                if self._seats[id][row][col] == 0:
                    self._seats[id][row][col] = 1
                    print(f'seat row-{row} and col-{col} Booked Success,For Show {id}')
                else:
                    print(f'seat {row} and {col} Already Booked')
            else:
                print(f'seat {row} and {col} is Invalid')
      
        
# ------------------------------------------------------------------------------          

    def view_show_list(self):
        print("\n\tHere is show list:-")
        for avialbe_show in self._show_list:
            print(avialbe_show)
# ------------------------------------------------------------------------------
    def view_available_seats(self, id):
        if id not in self._seats:
            print("invalid id..!!!")
            return
        print(f'\n\t Availabel sits for id-{id}')
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 0:
                    # print(f'rows {i} ,cols {j} : now availabe')
                    print("0" , end=" ") # 0 mane Blank seat
                else:
                    print('1',  end = " ") # 1 mane Booked seat
            print()
            
# ------------------------------------------------------------------------------

Hall_1 = Hall(rows=5, cols=5, hall_no=110)

Admin = Hall_1.entry_show(id=11, movie_name='3_iditos', time="10.00 am\n")
Srk = Hall_1.entry_show(id=12, movie_name='4_iditos', time="11.00 am\n")
Solmon_vhai= Hall_1.entry_show(id=13, movie_name='5_iditos', time="12.00 am\n")

# Hall_1.view_show_list()

# Hall_1.Book_Seats(id=11, seat_wanna_book=[(0,3),(4,0)])

# Hall_1.view_available_seats(id =11)

Run = True
CurrentUser = Admin 
while Run :
    print("Options:-\n")
    print("1.View All show today")
    print("2.View Available tickets")
    print("3.Book ticket")
    print("4.Exit")

    ch = int(input("\nEnter Option:-"))

    if ch== 1:
        Hall_1.view_show_list()

    elif ch == 2:
        id = int(input("\tEnter id:"))
        Hall_1.view_available_seats(id)
    
    elif ch == 3:
        print("Ticket Booking Process:-")

        id = int(input("\t1.Enter id:-"))
        Ticket = int(input("\t2.Number of tickets:-"))
        Row = int(input("\t2.Enter Row:-"))
        Col = int(input("\t2.Enter Col:-"))
        sit_row_col = [(Row,Col)]

        Hall_1.Book_Seats(id, sit_row_col)
    else:
        CurrentUser = None
        print("You Successfullly Exited Now...!")

       
        

