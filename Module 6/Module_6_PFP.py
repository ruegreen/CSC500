#import datetime lib for date formating in main function
import datetime

#Define the ItemToPurchase Class
class ItemToPurchase(object):
    #set the default values in the constructor if they are not passed when creating an instance of the class
    def __init__(self,name="none",description="none",price=0,qty=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = qty

    #Function prints out current object's attributes
    def print_cost_item(self):
        print(f"{self.item_name}, Quantity: {self.item_quantity} @ ${self.item_price} = ${int(self.item_quantity)*int(self.item_price)}")

    #Function prints out the current objects item name and description only
    def print_description_item(self):
        print(f"{self.item_name}, Description: {self.item_description}")

class ShoppingCart(object):
     #set the default values in the constructor if they are not passed when creating an instance of the class
    def __init__(self,customer_name="none",current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date=current_date
        self.cart_items = []
        self.total_cost = 0

    #define a method to add an object of type ItemToPurchase to the shopping cart list cart_items
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        self.total_cost += ItemToPurchase.item_quantity*ItemToPurchase.item_price

    #define a method to remove an object of type ItemToPurchase from the shopping cart list cart_items
    def remove_item(self,item_name):
        #Boolean to track if removal was a success
        removed = False
        #Loop through the objects in the cart_items
        for item in self.cart_items:
            #If we found the item name in the object item_name then lets remove it
            if item_name in item.item_name:
                #Update the class variable total_cost to reflect the removed item
                self.total_cost -= item.item_quantity*item.item_price
                #Remove the object from the list
                self.cart_items.remove(item)
                #set the removed boolen to true
                removed=True
        #print out the message whether it was removed or not
        if(removed):
             print(f"Removed item with name: {item_name} from your cart!")
        else:
            print(f"Item with name: {item_name} was not found in your shopping cart, nothing removed!")

    def modify_item(self, ItemToPurchase):
        #Set a booleand to track if we modified an item in the cart
        modified = False
        #Loop through the item objects in the cart_items list
        for item in self.cart_items:
            #If we found the item that we want to modify then we need to check to see if it doesnt have the default values from the constructor
            if ItemToPurchase.item_name in item.item_name:
                #If it doesnt have the default values from the class constructor then we need to modify it
                if ((item.item_description != "none") or (item.item_price != 0) or (item.item_quantity != 0)):
                    #Remove the old cost out of the class variable total_cost
                    self.total_cost -= item.item_quantity*item.item_price
                    #Updated the item object with the new values, could also do this by just replacing the entire object but went with direct assignments
                    item.item_description = ItemToPurchase.item_description
                    item.item_price = ItemToPurchase.item_price
                    item.item_quantity = ItemToPurchase.item_quantity
                    #Update the class variable total_cost with the new cost based on new quantity and price
                    self.total_cost += item.item_quantity*item.item_price
                    #set the modified boolean to true 
                    modified = True
        #Print out the correct message depending on whether the record was modified
        if(modified):
             print(f"Updated item with name: {ItemToPurchase.item_name} in your cart!")
        else:
            print(f"Item with name: {ItemToPurchase.item_name} was not found in your shopping cart, nothing was modified")

    #Method returns the number of items in the cart, does this by returning the len of the cart_items list which is a list of ItemsToPurchase objects
    def get_num_items_in_cart(self):
        return(len(self.cart_items))

    #Method that returned the class variable total_cost which is updated during Add, Remove and Change operations (CRUD) functions
    def get_cost_of_cart(self):
        return(self.total_cost)

    #Method that prints the Total of the shopping cart
    def print_total(self):
        #Check to see if the shopping cart is empty, if not print the contents, if its empty print a Shopping cart is empty message
        if(self.get_num_items_in_cart() == 0):
            print("Shopping Cart is EMPTY!")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            #Print out each item in the cart_items list
            for item in self.cart_items:
                #Call the class function print_cost_item() which outputs the current item's attributes
                item.print_cost_item()
            #print out the total cost of the shopping cart using a class method that returns a class variable total_cost
            print(f"Total: ${self.get_cost_of_cart()}")

    #Method that prints the item and descriptions that are in the shopping cart
    def print_description(self):
        #Check to see if the shopping cart is empty, if not print the contents, if its empty print a Shopping cart is empty message
        if(self.get_num_items_in_cart() == 0):
            print("Shopping Cart is EMPTY!")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            print(f"Item Descriptions")
            #Loop through and print the the item name and description, this is calling a method in the ItemToPurchase class
            for item in self.cart_items:
                #Call the class function print_decription_item() which outputs the current item's attributes
                item.print_description_item()
            
#Main function
def main():
    #Static menu options
    menu_options = {
        1: 'a - Add item to cart',
        2: 'r - Remove item from cart',
        3: 'c - Change item quantity',
        4: 'i - Output items\' descriptions',
        5: 'o - Output shopping cart',
        6: 'q - Quit',
    }
    
    #function that prints the menu and controls the options on the menu
    def print_menu(shopping_cart):
        #Print the actual menu to the console
        for key in menu_options.keys():
            print (menu_options[key] )
        #get the users menu choice
        option = input('Enter your choice: ')
        #If else block to handle the different menu choices
        if option == "a":
            item_name = input("Enter the name for item: ")
            item_description = input(f"Enter a description for {item_name}: ")
            item_price = input(f"Enter the price for {item_name}: $")
            item_quantity = input(f"Enter the quantity of {item_name}: ")
            print("\n")
            #call the class method for adding an item and pass in the ItemToPurchase instance once its created inline
            shopping_cart.add_item(ItemToPurchase(item_name,item_description,int(item_price),int(item_quantity)))
        elif option == "r":
            item_name = input("What is the name of the item you would like to remove? ")
            #call the class method to remove an item from the shopping cart, method using the name of the item to remove it
            shopping_cart.remove_item(item_name)
        elif option == "c":
            item_name = input("Enter the name for item you would like to update: ")
            item_description = input(f"Enter a new description for {item_name}: ")
            item_price = input(f"Enter a new price for {item_name}: $")
            item_quantity = input(f"Enter a new quantity for {item_name}: ")
            print("\n")
            #call the class methodto modify an item, create an ItemToPurchase which will be used to update the object in the existing shopping cart list
            shopping_cart.modify_item(ItemToPurchase(item_name,item_description,int(item_price),int(item_quantity)))
        elif option == "i":
            #Print out just the item name and description calling the class method
            shopping_cart.print_description()
        elif option == "o":
            #Print out the shopping cart and include each item and a grand total
            shopping_cart.print_total()
        elif option == "q":
            #Exit the program
            print('Thank you for shopping with us!')
            exit()
        else:
            print('Invalid choice! Please select from the following choices:')

    #Method that uses a datetime object to add the correct suffix to the day of the month Ex: th, rd, nd, st 
    def fix_day_suffix(today):
        day = today.day
        #check the range of the day in the month and apply the correct suffix
        if (3 < day < 21) or (23 < day < 31):
            day = str(day) + 'th'
        else:
            suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
            day = str(day) + suffixes[day % 10]
        #return the day with the correct suffix as a string    
        return(day)

    #Clear the console and ask for the customers name
    print(chr(27) + "[2J")
    customer_name = input("What is your name? ")
    today = datetime.datetime.now()
    #Format the date and use # for a placeholder to replace and insert the day correct suffix
    current_date = today.strftime("%B #, %Y")
    #call method to get the correct day suffix and use the string replace function to replace our # placeholder from previous step
    current_date = current_date.replace('#', fix_day_suffix(today))
    #Create an instance of the shopping cart passing the customers name and the current date
    shopping_cart = ShoppingCart(customer_name,current_date)
    print(f"Welcome {shopping_cart.customer_name}, today is: {shopping_cart.current_date}. Lets start shopping!")
    #Start the menu loop and call the print_menu method passing the instance of the shopping cart created earlier
    while(True):
        print_menu(shopping_cart)
        
if __name__ == "__main__":
    main()

