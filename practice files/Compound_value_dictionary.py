def main():
    #create a dictionary with student IDs as the keys
    #and student data stored in a list as the values.
    students={
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" ,"dav19008@byui.edu", 0]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    #Get a student ID from the user.

    #id=input("Enter a student ID: ")

     
     #This is a difficult and slow way to find an item in a dictionary. 
     #I tried running it and nothing happened. I think it terminated.
    #student=None
    #for key,value in students.items():
        #if key==id:
            #student=value
            #break
        
    #instead, use this

    #if id in students:
        #value=students[id]
        #print(value)
    #else:
        #print("Nah it ain't here")

    #The lines of code above would print out the whole list of a particular ID
    #The proper thing to do if you want a particular element from a list is:

    #if id in students:
       # value=students[id]
       # email=value[EMAIL_INDEX]
        #print(f"{email}")
    #else:
        #print(" I don't  see it...")   

    #Processing all the items in a dictionary
    #this is done using a for loop and the dict.items() method
    #the one i commented as a slow and difficult process earlier
    #it was slow for that task but for this one, it's simple and faster

    total=0
    for key, value in students.items():
        credits= value[CREDITS_INDEX]
        total += credits
    print(f"Total credits earned by all students: {total}")

#call main to start this program
if __name__ =="__main__":
     main()