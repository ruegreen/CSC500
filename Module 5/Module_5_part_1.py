#Main function
def main():
    #Lets use a list to display the name of the month for user input
    months = ["January","February","March","April","May","June","July","August","September","October", "November","December"]
    #Initialize the total rain fall for use in the inner loop
    total_rain = 0
    #Get the total years for the outer loop
    num_of_years = input("How many years would you like to calculate? ")
    #Setup a double loop, outer is the number of years, inner will be always be 12 months
    for y in range(int(num_of_years)):
        for m in range(12):
            #Using the list above, ask per month per the currrent year for the rain fall amount
            in_of_rain = input(f"How many inches of rain in year #{y+1} for {months[m]}: ")
            #Add the current months amount to the total for use on the final output and average calculation
            total_rain += float(in_of_rain)
    #Calculate the total number of months based on total years 
    total_months = int(num_of_years) * 12
    #Output the total months
    print(f"Total months: {total_months}")
    #Output the total rainfall for the total years and months, format and round to two decimal digits
    print("Total rainfall: " + '{:,.2f}'.format(round(total_rain,2)) +  " inches (Rounded to two decimals)")
    #Output the average rainfall for the total years and months, format and round to two decimal digits
    print("Average rainfall: " + '{:,.2f}'.format(round(total_rain/total_months,2)) +  " inches (Rounded to two decimals)")

if __name__ == "__main__":
    main()