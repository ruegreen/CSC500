import datetime

class ItemToPurchase(object):
    #set the default values in the constructor if they are not passed when creating an instance of the class
    def __init__(self,name="none",description="none",price=0,qty=0):
        self.item_name = name
        self.description = description
        self.item_price = price
        self.item_quantity = qty

    #Function prints out current object's attributes
    def print_cost_item(self):
        print(f"{self.item_name}, Quantity: {self.item_quantity} @ ${self.item_price} = ${int(self.item_quantity)*int(self.item_price)}")

    #Function prints out the current objects item name and description only
    def print_description_item(self):
        print(f"{self.item_name}, Description: {self.description}")

class ShoppingCart(object):
     #set the default values in the constructor if they are not passed when creating an instance of the class
    def __init__(self,customer_name="none",current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date=current_date
        self.cart_items = []
        self.total_cost = 0

    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        self.total_cost += ItemToPurchase.item_quantity*ItemToPurchase.item_price

    def remove_item(self,item_name):
        removed = False
        for item in self.cart_items:
            if item_name in item.item_name:
                #Remember to adjust the cost of the cart!!
                self.total_cost -= item.item_quantity*item.item_price
                self.cart_items.remove(item)
                removed=True
        return(removed)

    def modify_item():
        #Remember to adjust the price of the cart, remove old cost, add new cost 
        pass

    def get_num_items_in_cart(self):
        return(len(self.cart_items))

    def get_cost_of_cart(self):
        return(self.total_cost)

    def print_total(self):
        if(self.get_num_items_in_cart() == 0):
            print("Shopping Cart is EMPTY!")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            for item in self.cart_items:
                #Call the class function print_cost_item() which outputs the current item's attributes
                item.print_cost_item()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_description(self):
        if(self.get_num_items_in_cart() == 0):
            print("Shopping Cart is EMPTY!")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            print(f"Item Descriptions")
            for item in self.cart_items:
                #Call the class function print_decription_item() which outputs the current item's attributes
                item.print_description_item()
            
#Main function
def main():
    menu_options = {
        1: 'a - Add item to cart',
        2: 'r - Remove item from cart',
        3: 'c - Change item quantity',
        4: 'i - Output items\' descriptions',
        5: 'o - Output shopping cart',
        6: 'q - Quit',
    }

    def print_menu():
        for key in menu_options.keys():
            print (menu_options[key] )

    def fix_day_suffix(today):
        #Now lets replace the # in the string to the correct day suffix ex: th st nd rd
        day = today.day
        if (3 < day < 21) or (23 < day < 31):
            day = str(day) + 'th'
        else:
            suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
            day = str(day) + suffixes[day % 10]
        return(day)

    #Clear the console and ask for the customers name
    print(chr(27) + "[2J")
    customer_name = input("What is your name? ")
    today = datetime.datetime.now()
    #Format the date and use # for a placeholder to replace and insert the day correct suffix
    current_date = today.strftime("%B #, %Y")
    #call out function to get the correct day suffix and use the string replace function to replace our # placeholder from previous step
    current_date = current_date.replace('#', fix_day_suffix(today))
    #Create and instance of the shopping cart
    shopping_cart = ShoppingCart(customer_name,current_date)
    #Clear the screen and print the welcome message using the customers name and todays date
    #print(chr(27) + "[2J")
    print(f"Welcome {shopping_cart.customer_name}, today is: {shopping_cart.current_date}. Lets start shopping!")
    while(True):
        print_menu()
        option = input('Enter your choice: ')
        if option == "a":
            print('Handle option \'Add\'')
            item_name = input("Enter the name for item: ")
            item_description = input(f"Enter a description for {item_name}: ")
            item_price = input(f"Enter the price for {item_name}: $")
            item_quantity = input(f"Enter the quantity of {item_name}: ")
            print("\n")
            #create an instance of ItemToPurchase
            #ItemToPurchase class constructor
            shopping_cart.add_item(ItemToPurchase(item_name,item_description,int(item_price),int(item_quantity)))
        elif option == "r":
            item_name = input("What is the name of the item you would like to remove? ")
            if(shopping_cart.remove_item(item_name)) == True:
                print(f"Removed item with name: {item_name} from your cart!")
            else:
                print(f"Item with name: {item_name} was not found in your shopping cart!")
        elif option == "c":
            print('Handle option \'Change\'')
        elif option == "i":
            shopping_cart.print_description()
        elif option == "o":
            shopping_cart.print_total()
        elif option == "q":
            print('Thank you for shopping with us!')
            exit()
        else:
            print('Invalid choice! Please select from the following choices:')

if __name__ == "__main__":
    main()

