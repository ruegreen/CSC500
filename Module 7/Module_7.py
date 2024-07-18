#Main function
def main():
    #Lets define our dicts for room_number, instructors and meeting_time
    room_number = { 
        "CSC101":"3004",
        "CSC102":"4501",
        "CSC103":"6755",
        "NET110":"1244",
        "COM241":"1411"
    }
    instructors = {
        "CSC101":"Haynes",
        "CSC102":"Alvardo",
        "CSC103":"Rich",
        "NET110":"Burke",
        "COM241":"Lee"
    }
    meeting_time = {
        "CSC101":"8:00 a.m.",
        "CSC102":"9:00 a.m.",
        "CSC103":"10:00 a.m.",
        "NET110":"11:00 a.m.",
        "COM241":"1:00 p.m."
    }
    while(True):
        #ask the user for the course number
        course_number = input("Please enter the course number, enter q to quit: ")
        #If they enter q, then quit the program
        if(course_number == "q"):
            exit()
        else:
            #Try to print out the course_number its meeting room, the instructor and the time by using the course number as the key for each dict we defined
            #earlier.  Use a try / except block to catch any invalid course_numbers entered by the user.  If its valid, print the reponse, if its not valid then
            #let them know and ask again for a vaild course number
            try:
                print(f"The course number {course_number} will be meeting in room {room_number[course_number]} with instructor {instructors[course_number]} at {meeting_time[course_number]}, dont be late!")
            except KeyError as e:
                print(f"Course number: {course_number} does not exist, please enter a valid course number!")
            

if __name__ == "__main__":
    main()