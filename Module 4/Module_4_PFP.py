#Create a class to store the items purchased
class ItemToPurchase(object):
    #set the default values in the constructor if they are not passed when creating an instance of the class
    def __init__(self,name="none",price=0,qty=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty

    #Function prints out current object's attributes
    def print_cost_item(self):
        print(f"Item: {self.item_name}, Quantity: {self.item_quantity} @ ${self.item_price} = ${int(self.item_quantity)*int(self.item_price)}")

#Main function
def main():
    #create an empty list which will holds the items purchased.  This will get repaced with a single instance of the shopping cart where the list of items
    #will be an attribute in the shopping cart class
    my_items = []
    
    #Collect the number of items purchased and create an object of the ItemToPurchase class and store it in the my_items list
    num_of_items = input("How many items are you purchasing today? ")
    for i in range(int(num_of_items)):
        item_name = input(f"Enter the name for item #{i+1}: ")
        item_price = input(f"Enter the price for {item_name}: $")
        item_quantity = input(f"Enter the quantity of {item_name}: ")
        print("\n")
        #create an instance of ItemToPurchase and append this new object using the append function for the list and pass in the values collected to the 
        #ItemToPurchase class constructor
        my_items.append(ItemToPurchase(item_name,int(item_price),int(item_quantity)))

    #Print the total cost looping through the objects stored in the my_items list
    print("TOTAL COST:", end="\n")
    total_cost = 0
    for item in my_items:
        #Call the class function print_cost_item() which outputs the current item's attributes
        item.print_cost_item()
        #store the total_cost by adding the current item price to the total_cost
        total_cost += item.item_quantity*item.item_price
    #printout out the total cost
    print(f"Your total for all items is: ${total_cost}")


if __name__ == "__main__":
    main()