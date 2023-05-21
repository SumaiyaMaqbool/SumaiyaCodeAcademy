class Restuarant:
    def __init__(self):
        self.menu_items ={}
        self.book_table =[]
        self.customer_orders =[]
    def add_item_to_menu(self,item, price):
        self.menu_items[item]= price
        
    def book_tables (self,table_number):
        self.book_table.append(table_number)
        
    def customer_order(self,table_number, order):
        self.order = order
        customer_orders.append(order)        
        return "Menu Item: {} Booked Table: {} Customer Order: {}".format(self.menu_items,self.book_table,self.customer_orders)
    
cus1= Restuarant(["pasta","rice","sweets","drinks"],2,{"rice","drinks"})
cus2= Restuarant(["pasta","rice","sweets","drinks"],1,{"pasta","drinks","sweets"})
print (cus1.customer_order())
print (cus2.customer_order())



