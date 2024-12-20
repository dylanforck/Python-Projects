#Import haslib module
import hashlib

#Import validation tools
from Validation_Tools import validUser, validPassword
from Validation_Tools import setStudentId, setName, setAge, setGender, setMajor, setPhoneNumber
from Validation_Tools import customInput

#Import SQL Alchemy session and classes
from SQL_Alchemy import session, User, Student, Score



#Login Display
#Create the display welcome function
def displayLogin(loginFile):
    
    #Open the file in read mode
    file = open(loginFile, 'r')
    
    #Display the contents of the file
    print(file.read())
    
    #Close the file
    file.close()
    


#Choice 1
#Create the login user function
def loginUser(accounts, loginFile):
    
    #Display the header
    print("===========================Login============================")
    
    #Loop to validate until correct entry is made
    while True:

        #Prompt the user for their username
        username = input("Please Enter Your Account: ")
        
        #Check for existing account
        if username in accounts:
            
            #Loop to validate until correct entry is made
            while True:

                #Prompt the user for their password
                password = input("Enter password: ")

                #Hash the password using MD5
                hashedPassword = hashlib.md5(password.encode()).hexdigest()
                
                #Check for correct passord
                if hashedPassword == accounts[username]:

                    #Return username
                    return username

                #If password is incorrect
                else:
    
                    #Display error message
                    print("\u274C Login Failed! Invalid Password")

        #If username does not exist
        else:

            #Display error message
            print("\u274C Login Failed! Account Does Not Exist")

            #Reinitiate main function
            main()
       


#Choice 2
#Create the register user function
def registerUser(accounts):

    #Display the header
    print("========================Registration========================")
    
    #Display the username validation rules
    print("1: Account Name is between 3 and 6 letters long"
        + "\n2: Account name's first letter must be capitalized")

    #Loop to validate until correct entry is made 
    while True:

        #Prompt the user for their username
        username = input("Please Enter Account Name: ")

        #Check for existing username
        if validUser(username, accounts) == 'existing':

            #Return to login menu
            return

        #Check for valid username
        elif validUser(username, accounts):

            #Break loop
            break
    
    #Display the password validation rules
    print("1: Password must start with one of the following special characters !@#$%^&*"
        + "\n2: Password must contain at least one digit, one lowercase letter, and one uppercase letter"
        + "\n3: Password must be between 6 and 12 letters long")

    #Loop to validate until correct entry is made 
    while True:

        #Prompt the user for their password
        password = input("Please Enter Password: ")

        #Check for valid password
        if validPassword(password):

            #Break loop
            break

    #Hash the password using MD5
    hashedPassword = hashlib.md5(password.encode()).hexdigest()
        
    #Set password for specific username in the accounts dictionary
    accounts[username] = hashedPassword

    #Display completion message
    print("\u2714 Registration Complete!")

    #Return accounts
    return accounts



#Choice 3
#Create the exit system function
def exitSystem(accounts, students, scores):

    #Prompt the user to confirm exiting the system
    confirm = input("Do you want to exit the system? Enter Y to confirm: ").upper()

    #If confirm is equal to yes
    if confirm == 'Y':

        #Saving the accounts dictionary to the user table
        for username, password in accounts.items():

            #Create a new User object for each account
            user = User(username=username, password=password)

            #Add the user to the session
            session.add(user)

        #Saving the students dictionary to the student table
        for studentId, student in students.items():

            #Create a students data object for each student
            studentsData = Student(id=studentId, name=student['name'], age=student['age'], gender=student['gender'], major=student['major'], phone=student['phone'])

            #Add the students data to the session
            session.add(studentsData)

        #Saving the scores dictionary to the 'score' table
        for studentId, score in scores.items():

            #Create a new scores data object for each student's scores
            scoresData = Score(id=studentId, name=score['name'], CS1030=score['CS 1030'], CS1100=score['CS 1100'], CS2030=score['CS 2030'])

            #Add the scores data to the session
            session.add(scoresData)

        #Commit all changes to the database
        session.commit()

        #Close the session
        session.close()

        #Return False to exit the system
        return False

    #If the user decides not to exit
    else:

        #Return to the main menu
        return


  
#Menu Display
#Create the display welcome function
def displayWelcome(welcomeFile, username):
    
    #Open the file in read mode
    file = open(welcomeFile, 'r')

    #Read the text in the file
    text = file.read()

    #Close the file
    file.close()

    #Replace %s with username variable
    userText = text.replace("%s", username)
    
    #Display the contents of the file
    print(userText)  
    


#Option 1
#Create the add student function
def addStudent(students, scores):

    #Display the validation rules for adding students 
    print("1: The first letter of the firstname and lastname must be capitalized"
            + "\n2: Firstname and lastname must each have at least two letters"
            + "\n3: No digits allowed in the name"
            + "\n4: Age must be between 0 and 100"      
            + "\n5: Gender can be M (Male), F (Female), or O (Other)"
            + "\n6: Phone must be in the (xxx-xxx-xxxx) format")

    #Invoke the set student ID function
    studentId = setStudentId(students)

    #Invoke the set name function
    name = setName(students)

    #Invoke the set age function
    age = setAge(students)

    #Invoke the set gender function
    gender = setGender(students)

    #Invoke the set major function
    major = setMajor(students)

    #Invoke the set phone number function
    phone = setPhoneNumber(students)

    #Add the new student information to the students dictionary
    students[studentId] = {'name': name, 'age': age, 'gender': gender, 'major': major, 'phone': phone}

    #Default scores to 0 for all courses
    cs1030 = 0
    cs1100 = 0
    cs2030 = 0

    #Add the new student information to the scores dictionary
    scores[studentId] = {'name': name, 'CS 1030': cs1030, 'CS 1100': cs1100, 'CS 2030': cs2030}

    #Display successful add student message
    print("\u2714 Student Added Successfully")

    #Return to main menu
    return



#Option 2
#Create function to show student
def showStudent(students):

    #Display the header
    print("========================Show Student========================")
    
    #Display show student menu options
    print("1: Show All Students"
        + "\n2: Show Students by Name"
        + "\n3: Show Students by ID"
        + "\nOther: Return")

    #Loop to validate until correct entry is made 
    while True:

        #Prompt the user for their submenu option
        subOption = int(input("Please Select: "))

        #Sub-Option 1
        if subOption == 1:

            #If students dictionary is empty
            if len(students) == 0:

                #Display no students in dictionary
                print("\u274C No students to display")

                #Return to main menu
                return
                
            #If condition above is not true
            else:

                #Display Header
                print("========================Student Record=======================")
                print(f"{'ID':<10}{'Name':<18}{'Age':<4}{'Gender':<7}{'Major':<6}{'\u260E':<12}")

                #Loop through each student ID and student in students dictionary
                for studentId, student in students.items():

                    #Set display variables
                    name = student['name']
                    age = student['age']
                    gender = student['gender']
                    major = student['major']
                    phone = student['phone']
                    
                    #Display the student ID row in the students dictionary
                    print(f"{studentId:<10}{name:<18}{age:<4}{gender:<7}{major:<6}{phone:<12}")

                #Return to main menu
                return

        #Sub-Option 2
        elif subOption == 2:

            #Prompt the user to enter the student name to be queried
            studentName = input("Please enter the student name you want to query: ")

            #Track records that are found
            found = 0

            #Create header flag variable
            headerFlag = True

            #Loop through each student ID and student in students dictionary
            for studentId, student in students.items(): 

                #Check if student name matches students dictionary value
                if student['name'] == studentName:

                    #Header flag logic to only show once
                    if headerFlag == True:  

                        #Display Header
                        print("========================Student Record=======================")
                        print(f"{'ID':<10}{'Name':<18}{'Age':<4}{'Gender':<7}{'Major':<6}{'\u260E':<12}")

                        #Update header flag
                        headerFlag = False

                    #Set display variables
                    name = student['name']
                    age = student['age']
                    gender = student['gender']
                    major = student['major']
                    phone = student['phone']
                    
                    #Display the student ID row in the students dictionary
                    print(f"{studentId:<10}{name:<18}{age:<4}{gender:<7}{major:<6}{phone:<12}")

                    #Increment found by 1
                    found += 1

            #Check if entries were found
            if found > 0:

                #Return
                return

            #Display none found message
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student Name {studentName} record does not exist")

                #Return
                return

        #Sub-Option 3
        elif subOption == 3:

            #Prompt the user to enter the student ID to be queried
            studentId = str(input("Please enter the student ID you want to query: "))

            #Check if student ID exists in students dictionary
            if studentId in students:

                #Set display variables
                student = students[studentId]
                name = student['name']
                age = student['age']
                gender = student['gender']
                major = student['major']
                phone = student['phone']
                
                #Display Header
                print("========================Student Record=======================")
                print(f"{'ID':<10}{'Name':<18}{'Age':<4}{'Gender':<7}{'Major':<6}{'\u260E':<12}")

                #Display the student ID row in the students dictionary
                print(f"{studentId:<10}{name:<18}{age:<4}{gender:<7}{major:<6}{phone:<12}")

            #If condition above is not true
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student ID {studentId} Record Does Not Exist")

            #Return to main menu
            return

        #Other Sub-Option to Return to Main Menu
        else:

            #Return to main menu
            return



#Option 3
#Create the modify student function
def modifyStudent(students):

    #Prompt the user to enter the student ID they want to modify
    studentId = str(input("Please Enter Student ID to Modify: "))

    #Check if the student exists in the records
    if studentId in students:

        #Set display variables
        student = students[studentId]
        name = student['name']
        age = student['age']
        gender = student['gender']
        major = student['major']
        phone = student['phone']

        #Display Header
        print("========================Modify Student=======================")
        print(f"{'ID':<10}{'Name':<18}{'Age':<4}{'Gender':<7}{'Major':<6}{'\u260E':<12}")

        #Display the student ID row in the students dictionary
        print(f"{studentId:<10}{name:<18}{age:<4}{gender:<7}{major:<6}{phone:<12}")

        #Track number of fields that are not updated
        unchangedCount = 0

        #Track step 1
        step = 1
        
        #Invoke custom input function for age
        newAge = customInput(age, "New age", step)

        #Determine if age field was updated
        if newAge == age:

            #If new age is equal to age, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set student index of name equal to new name
            student['age'] = newAge

        #Track step 2
        step = 2

        #Invoke custom input function for major
        newMajor = customInput(major, "New major", step)

        #Determine if major field was updated
        if newMajor == major:

            #If new major is equal to major, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set major equal to new major
            student['major'] = newMajor

        #Track step 3
        step = 3

        #Invoke custom input function for phone number
        newPhone = customInput(phone, "New phone \u260E", step)

        #Determine if phone field was updated
        if newPhone == phone:

            #If new phone is equal to phone, increment by 1
            unchangedCount += 1

        #If condition above is not true
        else:

            #Set phone equal to new phone
            student['phone'] = newPhone

        #If no changes occurred
        if unchangedCount == 3:

            #Display that record was not modified
            print("\u274C Record not modified")

            #Return
            return

        #If condition above is not true
        else:

            #Display that record was not modified
            print("\u2714 Student record updated successfully")

            #Return
            return

    #If condition above is not true
    else:

        #Display specfic student ID does not exist
        print(f"\u274C Student ID {studentId} record does not exist")

        #Return
        return



#Option 4
#Create the delete student function
def deleteStudent(students, scores):

    #Display the header
    print("=======================Delete Student=======================")
    
    #Display show student menu options
    print("1: Delete Students by Name"
        + "\n2: Delete Students by ID"
        + "\nOther: Return")

    #Loop to validate until correct entry is made 
    while True:

        #Prompt the user for their submenu option
        subOption = int(input("Please Select: "))

        #Sub-Option 1
        if subOption == 1:

            #Prompt the user to enter the student name to be deleted
            studentName = input("Please Enter Student Name to Delete: ")

            #Create empty list for Student Name IDs
            studentNameIds = []
            
            #Loop through each student ID and student in students dictionary
            for studentId, student in students.items():

                #Check if student name matches students dictionary value
                if student['name'] == studentName:
                
                    #Add Student ID to Student Name IDs list
                    studentNameIds.append(studentId)
          
            #Check if IDs were found
            if len(studentNameIds) > 0:

                #Prompt the user to confirm exiting the system
                confirm = input("Delete Student? Enter Y to Confirm: ").upper()

                #If confirm is equal to yes
                if confirm == 'Y':

                    #Loop through matching IDs
                    for studentId in studentNameIds:

                        #Delete specific student from students dictionary
                        del students[studentId]

                        #Delete specific student from scores dictionary
                        del scores[studentId]               

                    #Display successful deletion message
                    print("\u2714 Record Deleted Successfully")

                #Return
                return

            #If condition above is not true
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student Name {studentName} record does not exist")

                #Return
                return

        #Sub-Option 2
        elif subOption == 2:

            #Prompt the user to enter the student ID to be queried
            studentId = str(input("Please Enter Student ID to Delete: "))

            #Check if student ID exists in students dictionary
            if studentId in students:

                #Prompt the user to confirm deletion of selected student
                confirm = input("Delete Student? Enter Y to Confirm: ").upper()

                #If confirm is equal to yes
                if confirm == 'Y':

                    #Delete specific student from the dictionary
                    del students[studentId]

                    #Delete specific student from scores dictionary
                    del scores[studentId]

                    #Display successful deletion message
                    print("\u2714 Record Deleted Successfully")

                #Return
                return

            #If condition above is not true
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student ID {studentId} Record Does Not Exist")

                #Return
                return

        #Other Sub-Option to Return to Main Menu
        else:

            #Return to main menu
            return



#Option 5
#Create function to display all students
def displayScores(scores):
    
    #Display the header
    print("========================Student Scores=======================")
    
    #Display show student menu options
    print("1: Display Student Score by Name"
        + "\n2: Update Student Score by ID"
        + "\nOther: Return")

    #Loop to validate until correct entry is made 
    while True:

        #Prompt the user for their submenu option
        subOption = int(input("Please Select: "))
        
        #Sub-Option 1
        if subOption == 1:

            #Prompt the user to enter the student name to be queried
            studentName = input("Please Enter Student Name: ")

            #Track records that are found
            found = 0

            #Create header flag variable
            headerFlag = True

            #Loop through each student ID and student in scores dictionary
            for studentId, student in scores.items():

                #Check if student name matches scores dictionary value
                if student['name'] == studentName:

                    #Header flag logic to only show once
                    if headerFlag == True:

                        #Display Header
                        print("========================Student Scores=======================")
                        print(f"{'ID':<10}{'Name':<18}{'CS 1030':<10}{'CS 1100':<10}{'CS 2030':<10}")

                        #Update header flag
                        headerFlag = False

                    #Set display variables
                    name = student['name']
                    cs1030 = student['CS 1030']
                    cs1100 = student['CS 1100']
                    cs2030 = student['CS 2030']
                    
                    #Display the student ID row in the scores dictionary
                    print(f"{studentId:<10}{name:<18}{cs1030:<10}{cs1100:<10}{cs2030:<10}")

                    #Increment found by 1
                    found += 1

            #Check if entries were found
            if found > 0:

                #Return
                return

            #Display none found message
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student Name {studentName} record does not exist")

                #Return
                return

        #Sub-Option 2
        elif subOption == 2:

            #Prompt the user to enter the student ID to be queried
            studentId = str(input("Please Enter Student ID for Score Update: "))

            #Check if student ID exists in scores dictionary
            if studentId in scores:

                #Set display variables
                student = scores[studentId]
                name = student['name']
                cs1030 = student['CS 1030']
                cs1100 = student['CS 1100']
                cs2030 = student['CS 2030']
                
                #Display Header
                print("========================Student Scores=======================")
                print(f"{'ID':<10}{'Name':<18}{'CS 1030':<10}{'CS 1100':<10}{'CS 2030':<10}")

                #Display the student ID row in the scores dictionary
                print(f"{studentId:<10}{name:<18}{cs1030:<10}{cs1100:<10}{cs2030:<10}")

                #Track number of fields that are not updated
                unchangedCount = 0

                #Request new score value
                newScore1030 = input("New Grade for CS 1030 (press enter without modification)")

                #Determine if score was updated
                if newScore1030 == '':

                    #If new score is equal to old score, increment by 1
                    unchangedCount += 1

                #If condition above is not true
                else:

                    #Set score index of course equal to new score
                    student['CS 1030'] = int(newScore1030)

                #Request new score value
                newScore1100 = input("New Grade for CS 1100 (press enter without modification)")

                #Determine if score was updated
                if newScore1100 == '':

                    #If new score is equal to old score, increment by 1
                    unchangedCount += 1

                #If condition above is not true
                else:

                    #Set score index of course equal to new score
                    student['CS 1100'] = int(newScore1100)

                #Request new score value
                newScore2030 = input("New Grade for CS 2030 (press enter without modification)")

                #Determine if score was updated
                if newScore2030 == '':

                    #If new score is equal to old score, increment by 1
                    unchangedCount += 1

                #If condition above is not true
                else:

                    #Set score index of course equal to new score
                    student['CS 2030'] = int(newScore2030)

                #If no changes occurred
                if unchangedCount == 3:

                    #Display that record was not modified
                    print("\u274C Record not modified")

                #If condition above is not true
                else:

                    #Display that record was not modified
                    print("\u2714 Student record updated successfully")

                #Return
                return

            #If condition above is not true
            else:

                #Display specfic student ID does not exist
                print(f"\u274C Student ID {studentId} record does not exist")

                #Return
                return

                

#Create the main function
def main():

    #Set login file variable
    loginFile = 'login.txt'

    #Set welcome file variable
    welcomeFile = 'student.txt'

    #Create blank dictionary to store accounts
    accounts = {}
    
    #Create blank dictionary to store students
    students = {}

    #Create blank dictionary to store sscores
    scores = {}  

    #Query the user table
    usersData = session.query(User).all()

    #Loop through each user object
    for user in usersData:

        #Populate the accounts dictionary
        accounts[user.username] = user.password

    #Query the Student table
    studentsData = session.query(Student).all()

    #Loop through each student object
    for student in studentsData:

        #Populate the students dictionary
        students[student.id] = {'name': student.name, 'age': student.age, 'gender': student.gender, 'major': student.major, 'phone': student.phone}

    #Query the Score table
    scoresData = session.query(Score).all()

    #Loop through each score object
    for score in scoresData:

        #Populate the scores dictionary
        scores[score.id] = {'name': score.name, 'CS 1030': score.CS1030, 'CS 1100': score.CS1100, 'CS 2030': score.CS2030}

    #While loop to keep running the system
    while True:
        
        #Invoke the display welcome function
        displayLogin(loginFile)

        #Prompt user for a menu choice
        choice = int(input("Please select (1-3): "))

        #Choice 1 
        if choice == 1:

            #Invoke login user function
            username = loginUser(accounts, loginFile)

            #While loop to keep running the system
            while True:
                
                #Invoke the display welcome function
                displayWelcome(welcomeFile, username)
                
                #Prompt user for a menu option
                option = int(input("Choose an option (1-6): "))

                #Option 1 
                if option == 1:

                    #Invoke add student function
                    addStudent(students, scores)
                    
                #Option 2
                elif option == 2:

                    #Invoke show student function
                    showStudent(students)         

                #Option 3
                elif option == 3:

                    #Invoke modify student function
                    modifyStudent(students)

                #Option 4
                elif option == 4:

                    #Invoke delete student function
                    deleteStudent(students, scores)

                #Option 5
                elif option == 5:

                    #Invoke display scores function
                    displayScores(scores)

                #Option 6
                elif option == 6:

                    #Break loop
                    break

                #If condition above is not true
                else:

                    #Display error message
                    print("\u274C Invalid option. Please try again.")
   
        #Choice 2
        elif choice == 2:

            #Invoke register user function to populate accounts
            accounts = registerUser(accounts)

        #Choice 3
        elif choice == 3:

            #Invoke exit system function, check for False
            if exitSystem(accounts, students, scores) is False:

                #Exit the system
                return

        #If condition above is not true
        else:

            #Display error message
             print("\u274C Invalid option. Please try again.")



#Run the program
main()
