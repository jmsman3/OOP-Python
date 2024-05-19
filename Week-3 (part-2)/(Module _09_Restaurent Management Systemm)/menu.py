
class Menu:
    def __init__(self):
        self.items = [] #items er database

    def add_new_item(self, item):
        self.items.append(item)
        print(f"Yes,{item.name} adding done...!")
    
    def find_item(self,item_name): # find_item function ta banano hoise remove item bananor jonno
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None 
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item is not None: #Shudhu if item: airokom likhle o hoi
            self.items.remove(item)
            print(f"item {item.name}  deleted")
        else:
            print(f"item {item.name} not found")
    
    def show_menu(self):
        print("=====Menu=====")
        print("Name\tPrice\tQuantity")
        for item in self.items :
            print(f"{item.name}\t{item.price}\t{item.quantity}")