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

    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item():
        pass

    def modify_item():
        pass

    def get_num_items_in_cart():
        pass

    def get_cost_of_cart():
        pass

    def print_total(self):
        if(len(self.cart_items) == 0):
            print("Shopping Cart is EMPTY!")
            pass
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {len(self.cart_items)}")
        total_cost = 0
        for item in self.cart_items:
            #Call the class function print_cost_item() which outputs the current item's attributes
            item.print_cost_item()
            #store the total_cost by adding the current item price to the total_cost
            total_cost += item.item_quantity*item.item_price
        print(f"Total: ${total_cost}")

    def print_description(self):
        if(len(self.cart_items) == 0):
            print("Shopping Cart is EMPTY!")
            pass
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {len(self.cart_items)}")
        print(f"Item Descriptions")
        total_cost = 0
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
            item_description = input(f"Enter a description for {item_name} ")
            item_price = input(f"Enter the price for {item_name}: $")
            item_quantity = input(f"Enter the quantity of {item_name}: ")
            print("\n")
            #create an instance of ItemToPurchase
            #ItemToPurchase class constructor
            shopping_cart.add_item(ItemToPurchase(item_name,item_description,int(item_price),int(item_quantity)))
        elif option == "r":
            print('Handle option \'Remove\'')
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

