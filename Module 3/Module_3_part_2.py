
#import datetime for use to calculate the time delta
import datetime

#function that calculates the time delta and extracts the substring of the time
def calculate_alarm(current_time, alarm_hrs):
  #Lets take the hour out of the string and store it in a newtime object
  newtime = datetime.datetime.strptime(current_time, "%H")
  #Lets now add the alarm_hrs to the newtime object
  newtime += datetime.timedelta(hours=int(alarm_hrs))
  #Finally lets cast the newtime value to a string and use the substring start and end to extract the newtime which includes the alarm_hrs
  print(f"\nYour alarm will go off at: {str(newtime)[11:16]} (Assuming a 24hr clock format)", end="\n")
    

def main():
    #The current time in hours assuming a 24 hr clock format
    print("\nWhat is the current time in hours (Assume a 24hr clock format)? ", end=" ")
    current_time = input()
    print("How many hours would you like your alarm set for?", end=" ")
    alarm_hrs= input()
    #call calculate_alarm, pass it the current time and alarm offset.  Output the time the alarm will go off
    calculate_alarm(current_time,alarm_hrs)
    
    
if __name__ == "__main__":
    main()