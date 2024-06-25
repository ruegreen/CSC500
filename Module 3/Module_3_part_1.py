def Total_Cost(food_cost):
    #calculate sales tax and tip remember, sales_tax and tip is only calculated off food cost and doesnt include each other!
    #clean up any values by rounding to two decimals
    food_cost = round(food_cost,2)
    sales_tax = round(food_cost * .07,2)
    tip = round(food_cost * .18,2)
    #Using the format statement, format the float as money for food_cost, sales_tax and tip, print each of them per line.
    print("\nYour food charge was:" + '${:,.2f}'.format(food_cost), end=" ")
    print("\nYour 7% sale tax will be: " + '${:,.2f}'.format(sales_tax),end=" ")
    print("\nYour 18% tip will be: " + '${:,.2f}'.format(tip), end=" ")
    #Using the format statement, format the float as money for total cost adding each item together
    print(f"\nTotal Cost of food will be: " + '${:,.2f}'.format(food_cost+sales_tax+tip), end="\n")
    
def main():
    #Get the users food cost
    print("The following program will ask you the charge for your food and will apply a tip and calculate sale tax.\n")
    print("How much did you food cost? ", end=" ")
    food_cost = float(input())
    #call Total_Cost to calculate and display, food_cost, sales_tax and tip 
    Total_Cost(food_cost)
    
if __name__ == "__main__":
    main()