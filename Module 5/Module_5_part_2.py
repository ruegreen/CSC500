#Define a function that acts like a switch statement since Python doesnt really have one.  In version 3.10 they introduced match and case keywords to
#implement a case statement
def switch(num_of_books):
        #Use the following conditionals to return the number of points earned
        if (int(num_of_books) > 0) and (int(num_of_books) < 2):
            return "You have earned 0 book club points"
        elif (int(num_of_books) >= 2) and (int(num_of_books) < 4):
            return "You have earned 5 book club points"
        elif (int(num_of_books) >= 4) and (int(num_of_books) < 6):
            return "You have earned 15 book club points"
        elif (int(num_of_books) >= 6) and (int(num_of_books) < 8):
            return "You have earned 30 book club points"
        elif (int(num_of_books) >=8):
            return "You have earned 60 book club points"
        
#Main function      
def main():
    #Ask the user how many books they purchased this month
    num_of_books = input("How many books have you purchased this month? ")
    #Pass this to our switch function defined above and print out the text that the function returns
    print(switch(num_of_books))
    
if __name__ == "__main__":
    main()