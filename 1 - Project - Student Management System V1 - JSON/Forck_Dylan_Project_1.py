#Dylan Forck
#Project
#Description: Student Management System - JSON



#Import json module
import json

#Import os module
import os


#Create the json read function, set students default to empty dictionary
def jsonRead(jsonFile, students={}):
    
    #Check if the student json file exists
    if os.path.exists(jsonFile):
        
        #Open the file in read mode
        file = open(jsonFile, 'r')
        
        #Load the data from the json file
        students = json.load(file)
        
        #Close the file
        file.close()
        
        #Return the loaded student data
        return students
    
    #Return default empty dictionary if file does not exist
    return students


#Create the json write function
def jsonWrite(jsonFile, students):
    
    #Open the file in write mode
    file = open(jsonFile, 'w')
    
    #Dump the data to the json file
    json.dump(students, file)
    
    #Close the file
    file.close()


#Menu Display
#Create the display welcome function
def displayWelcome(welcomeFile):
    
    #Open the file in read mode
    file = open(welcomeFile, 'r')
    
    #Display the contents of the file
    print(file.read())
    
    #Close the file
    file.close()



#Option 1
#Create the add student function
def addStudent(students):

    #Display the validation rules for adding students 
    print("1: The first letter of the firstname and lastname must be capitalized"
            + "\n2: Firstname and lastname must each have at least two letters"
            + "\n3: No digits allowed in the name"
            + "\n4: Student ID is 6 digits long which starts with 700"
            + "\n5: Phone must be in the (xxx-xxx-xxxx) format"
            + "\n6: Student major must be in CS, CYBR, SE, IT, or DS")

    #Invoke the set student ID function
    studentId = setStudentId(students)

    #If condition if loop returns False
    if studentId is False:

        #Return to main menu
        return

    #Invoke the set name function
    name = setName(students)

    #Invoke the set phone number function
    phone = setPhoneNumber(students)

    #Invoke the set major function
    major = setMajor(students)

    #Add the new student information to the students dictionary
    students[studentId] = {"name": name, "phone": phone, "major": major}

    #Display successful add student message
    print("\u2714 New student record has been added")

    #Return to main menu
    return


#Create the set student ID function
def setStudentId(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a student id
        studentId = input("Please enter the student ID: ")

        #Check if student ID has exactly 6 digits 
        if len(studentId) != 6:

            #Display error message
            print("\u274C Invalid student ID")

        #Check if student ID is only digits    
        elif not studentId.isdigit():

            #Display error message
            print("\u274C Invalid student ID")

        #Check if student ID starts with 700
        elif not studentId.startswith("700"):

            #Display error message
            print("\u274C Invalid student ID")

        #Check if student ID already exists
        elif studentId in students:

            #Display error message
            print("\u274C Student ID already exists in the system, please enter a different ID")

            #Return False to terminate loop
            return False

        #If none of the above are true
        else:

            #Return student ID
            return studentId


#Create the set name function
def setName(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a student name
        name = input("Please enter the student name (Firstname Lastname): ")

        #Split firstname and lastname using split method to create list
        nameSplit = name.split()

        #Check if namesplit contains two names 
        if len(nameSplit) < 2:

            #Display error message
            print("\u274C Invalid student name")

        #If none of the above are true
        else:

            #Set firstname to name split list index of 0
            firstname = nameSplit[0]

            #Set lastname to name split list index of 1
            lastname = nameSplit[1]
            
            #Check if firstname and lastname are capitalized 
            if not (firstname.istitle() and lastname.istitle()):  

                #Display error message
                print("\u274C Invalid student name")

            #Check if firstname and lastname are less than 2 letters 
            elif len(firstname) < 2 or len(lastname) < 2:

                #Display error message
                print("\u274C Invalid student name")

            #Check if firstname and lastname are alphabetic
            elif not (firstname.isalpha() and lastname.isalpha()):

                #Display error message
                print("\u274C Invalid student name")

            #If none of the above are true
            else:

                #Return student name
                return name


#Create the set phone number function
def setPhoneNumber(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a phone number
        phone = input("Please enter the student phone \u260E: ")
        
        #Check if phone number is 12 characters 
        if len(phone) != 12:  

            #Display error message
            print("\u274C Invalid phone number")

        #Check to make sure only digits are included in the ranges below
        elif not phone[:3].isdigit() or not phone[4:7].isdigit() or not phone[8:].isdigit():

            #Display error message
            print("\u274C Invalid phone number")

        #Check if dashes are included at the 4th and 8th characters
        elif phone[3] != '-' or phone[7] != '-':

            #Display error message
            print("\u274C Invalid phone number")

        #If none of the above are true
        else:

            #Return phone number
            return phone


#Create the set major function
def setMajor(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a major
        major = input("Please enter the student major: ").upper()

        #Create list of majors
        majorsList = ["CS", "CYBR", "SE", "IT", "DS"]
        
        #Check if major is in the majors list 
        if major not in majorsList:  

            #Display error message
            print("\u274C Invalid major")

        #If none of the above are true
        else:

            #Return major
            return major



#Option 2
#Create the delete student function
def deleteStudent(students):

    #Prompt the user to input a student ID
    studentId = input("Enter student ID to delete: ") 

    #Check if the student ID exists in the students dictionary
    if studentId in students:

        #Set variables from index of student ID as student
        student = students[studentId]
        name = student['name']
        phone = student['phone']
        major = student['major']

        #Display the specific student ID row in the students dictionary
        print(f"\u2709 ID: {studentId}, Name: {name}, Phone: {phone}, Major: {major}")

        #Prompt the user to confirm deletion of selected student
        confirm = input("Are you sure you want to delete the record? Y or N: ").upper()

        #If confirm is equal to yes
        if confirm == 'Y':

            #Delete specific student from the dictionary
            del students[studentId]

            #Display successful deletion message
            print("\u2714 Student record deleted")

        #If condition above is not true
        else:

            #Display cancled deletion message
            print("Deletion canceled.")

    #If condition above is not true
    else:

        #Display specfic student ID does not exist
        print(f"\u274C Student ID {studentId} record does not exist")



#Option 3
#Create the modify student function
def modifyStudent(students):

    #Prompt the user to enter the student ID they want to modify
    studentId = input("Enter student ID to modify: ")

    #Check if the student exists in the records
    if studentId in students:

        #Set variables from index of student ID as student
        student = students[studentId]
        name = student['name']
        phone = student['phone']
        major = student['major']

        #Display the specific student ID row in the students dictionary
        print(f"\u2709 ID: {studentId}, Name: {name}, Phone: {phone}, Major: {major}")

        #Track number of fields that are not updated
        unchangedCount = 0

        #Track step 1
        step = 1
        
        #Invoke custom input function for name
        newName = customInput(name, "New name", step)

        #Determine if name field was updated
        if newName == name:

            #If new name is equal to name, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set name equal to new name
            name = newName

        #Track step 2
        step = 2

        #Invoke custom input function for phone number
        newPhone = customInput(phone, "New phone \u260E", step)

        #Determine if phone field was updated
        if newPhone == phone:

            #If new phone is equal to phone, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set phone equal to new phone
            phone = newPhone

        #Track step 3
        step = 3

        #Invoke custom input function for major
        newMajor = customInput(major, "New major", step)

        #Determine if major field was updated
        if newMajor == major:

            #If new major is equal to major, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set major equal to new major
            major = newMajor

        #If no changes occurred
        if unchangedCount == 3:

            #Display that record was not modified
            print("\u274C Record not modified")

        #If condition above is not true
        else:

            #Display that record was not modified
            print("\u2714 Student record updated successfully")

            #Update the student information in the students dictionary
            students[studentId] = {"name": name, "phone": phone, "major": major}

    #If condition above is not true
    else:

        #Display specfic student ID does not exist
        print(f"\u274C Student ID {studentId} record does not exist")


#Create the custom input function
def customInput(currentValue, message, step):
        
    #Loop to validate until correct entry is made for name  
    while step == 1:

        #Prompt the user to input new value or hit enter to keep current value
        name = input(f"{message} (press enter without modification): ")

        #If new value is empty
        if name == "":

            #Return current value
            return currentValue

        #If condition above is not true
        else:

            #Split firstname and lastname using split method to create list
            nameSplit = name.split()

            #Check if namesplit contains two names 
            if len(nameSplit) < 2:

                #Display error message
                print("\u274C Invalid student name")

            #If none of the above are true
            else:

                #Set firstname to name split list index of 0
                firstname = nameSplit[0]

                #Set lastname to name split list index of 1
                lastname = nameSplit[1]
                
                #Check if firstname and lastname are capitalized 
                if not (firstname.istitle() and lastname.istitle()):  

                    #Display error message
                    print("\u274C Invalid student name")

                #Check if firstname and lastname are less than 2 letters 
                elif len(firstname) < 2 or len(lastname) < 2:

                    #Display error message
                    print("\u274C Invalid student name")

                #Check if firstname and lastname are alphabetic
                elif not (firstname.isalpha() and lastname.isalpha()):

                    #Display error message
                    print("\u274C Invalid student name")

                #If none of the above are true
                else:

                    #Return student name
                    return name

    #Loop to validate until correct entry is made for phone number   
    while step == 2:

        #Prompt the user to enter a phone number
        phone = input(f"{message} (press enter without modification): ")

        #If new value is empty
        if phone == "":

            #Return current value
            return currentValue

        #If condition above is not true
        else:
        
            #Check if phone number is 12 characters 
            if len(phone) != 12:  

                #Display error message
                print("\u274C Invalid phone number")

            #Check to make sure only digits are included in the ranges below
            elif not phone[:3].isdigit() or not phone[4:7].isdigit() or not phone[8:].isdigit():

                #Display error message
                print("\u274C Invalid phone number")

            #Check if dashes are included at the 4th and 8th characters
            elif phone[3] != '-' or phone[7] != '-':

                #Display error message
                print("\u274C Invalid phone number")

            #If none of the above are true
            else:

                #Return phone number
                return phone

    #Loop to validate until correct entry is made for major  
    while step ==  3:

        #Prompt the user to enter a major
        major = input(f"{message} (press enter without modification): ").upper()

        #If new value is empty
        if major == "":

            #Return current value
            return currentValue

        #If condition above is not true
        else:

            #Create list of majors
            majorsList = ["CS", "CYBR", "SE", "IT", "DS"]
            
            #Check if major is in the majors list 
            if major not in majorsList:  

                #Display error message
                print("\u274C Invalid major")

            #If none of the above are true
            else:

                #Return major
                return major



#Option 4
#Create function to query specific student 
def queryStudent(students):

    #Prompt the user to enter the student ID to be queried
    studentId = input("Please enter the student ID you want to query: ")

    #Check if student ID exists in students dictionary
    if studentId in students:

        #Set display variables from index of student ID as student
        student = students[studentId]
        name = student['name']
        phone = student['phone']
        major = student['major']

        #Display the specific student ID row in the students dictionary
        print(f"\u2709 ID: {studentId}, Name: {name}, Phone: {phone}, Major: {major}")

    #If condition above is not true
    else:

        #Display specfic student ID does not exist
        print(f"\u274C Student ID {studentId} record does not exist")



#Option 5
#Create function to display all students
def displayAllStudents(students):
    
    #If students dictionary is empty
    if len(students) == 0:

        #Display no students in database
        print("\u274C No students to display")
        
    #If condition above is not true
    else:

        #Loop through each student ID in students dictionary
        for studentId in students:

            #Set display variables from index of student ID as student
            student = students[studentId]
            name = student['name']
            phone = student['phone']
            major = student['major']

            #Display the student ID row in the students dictionary
            print(f"ID: {studentId}, Name: {name}, Phone: {phone}, Major: {major}")



#Option 6
#Create the exit system function
def exitSystem(jsonFile, students):

    #Prompt the user to confirm exiting the system
    confirm = input("Do you want to exit the system? Enter Y to confirm: ").upper()

    #If confirm is equal to yes
    if confirm == 'Y':

        #Invoke the json write function to save the json file
        jsonWrite(jsonFile, students)

        #Return False to exit the system
        return False

    #If condition above is not true
    else:

        #Return to main menu
        return



#Create the main function
def main():

    #Set json file variable
    jsonFile = 'student.json'

    #Set welcome file variable
    welcomeFile = 'welcome.txt'
    
    #Load students by invoking the json read function
    students = jsonRead(jsonFile)

    #While loop to keep running the system
    while True:
        
        #Invoke the display welcome function
        displayWelcome(welcomeFile)
        
        #Prompt user for a menu option
        option = int(input("Choose an option (1-6): "))

        #Option 1 
        if option == 1:

            #Invoke add student function
            addStudent(students)
            
        #Option 2
        elif option == 2:

            #Invoke delete student function
            deleteStudent(students)

        #Option 3
        elif option == 3:

            #Invoke modify student function
            modifyStudent(students)

        #Option 4
        elif option == 4:

            #Invoke query student function
            queryStudent(students)

        #Option 5
        elif option == 5:

            #Invoke display all students function
            displayAllStudents(students)

        #Option 6
        elif option == 6:

            #Invoke exit system function, check for False
            if exitSystem(jsonFile, students) is False:

                #Exit the system
                break

        #If condition above is not true
        else:

            #Display error message
            print("\u274C Invalid option. Please try again.")



#Run the program
main()
