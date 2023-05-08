def main():
    #create a dictionary with student IDs as
    #the keys and student names as the values.
    students= {
        "42-039-4736": "Aragon SonofArathorn",
        "61-315-0160": "Frodo Baggins",
        "10-450-1203": "Samwise Gamgee",
        "75-421-2310": "Peregrin Took",
        "07-103-5621": "Meriadoc Brandybuck"
    }
    lsize=len(students)
    print(f"{students}, length: {lsize}")

    #Add an item to the dictionary
    students["81-298-9238"]="Gandalf TheGrey"
   
    #Remove an item from the dictionary
    students.pop("61-315-0160")
   

    #Get the number of items in the dictionary and print it
    length=len(students)
    print(f"length: {length}")

    #Print the entire dictionary
    print(students)
    print()

    #Get a student ID from the user
    id=input("Enter a student ID:")

    #Check if the student ID is in the dictionary
    if id in students:
        #Find the student ID in the dictionary and retrieve the corresponding student name
        name=students[id]
        #print student's name
        print(name)
    else:
        print("No such student")

#call main to start this program
if  __name__=="__main__":
    main()