class ItemToPurchase(object):
    def __init__(self,name="none",price=0,qty=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty

    def print_cost_item(self):
        print(f"Item: {self.item_name}, Quantity: {self.item_quantity} @ ${self.item_price} = ${int(self.item_quantity)*int(self.item_price)}")

def main():
    my_items = []

    num_of_items = input("How many items are you purchasing today? ")
    for i in range(int(num_of_items)):
        #my_items.append(ItemToPurchase("none",0,0))
        item_name = input(f"Enter the name for item #{i+1}: ")
        item_price = input(f"Enter the price for {item_name}: $")
        item_quantity = input(f"Enter the quantity of {item_name}: ")
        print("\n")
        my_items.append(ItemToPurchase(item_name,int(item_price),int(item_quantity)))
       
        #print(item_name)
        #my_items[i].item_name = item_name
        #my_items[i].item_price = item_price
        #my_items[i].item_name = item_quantity
        #print(my_items[i].item_name)
    

    print("TOTAL COST:", end="\n")

    total_cost = 0
    for item in my_items:
        item.print_cost_item()
        total_cost += item.item_quantity*item.item_price
    print(f"Your total for all items is: ${total_cost}")


if __name__ == "__main__":
    main()