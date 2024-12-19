#Dylan Forck
#700601692
#Project 2
#Description: Student Management System - Validation Tools



#Create the valid user function
def validUser(username, accounts):

    #Check for correct username length
    if len(username) < 3 or len(username) > 6:

        #Display error message
        print("\u274C Account Name Not Valid!")

        #Return False
        return False

    #Check for only alphabethical characters
    elif not username.isalpha():

        #Display error message
        print("\u274C Account Name Not Valid!")

        #Return False
        return False

    #Check for first letter capitalization
    elif not username.istitle():

        #Display error message
        print("\u274C Account Name Not Valid!")

        #Return False
        return False
    

    #Check for existing account
    elif username in accounts:

        #Display error message
        print("\u274C Registration Failed! Account Already Exists")

        #Return existing to return to login menu
        return 'existing'

    #If none of the above are True
    else:

        #Return True
        return True



#Create the valid password function
def validPassword(password):

    #Create the special characters variable
    specialChar = "!@#$%^&*"

    #Check for correct password length
    if len(password) < 6 or len(password) > 12:

        #Display error message
        print("\u274C Password Not Valid!")

        #Return False
        return False

    #Check for special character in password
    elif password[0] not in specialChar:

        #Display error message
        print("\u274C Password Not Valid!")

        #Return False
        return False

    #Check for digit in password
    elif not any(digit.isdigit() for digit in password):

        #Display error message
        print("\u274C Password Not Valid!")

        #Return False
        return False

    #Check for lower case letter in password
    elif not any(lower.islower() for lower in password):

        #Display error message
        print("\u274C Password Not Valid!")

        #Return False
        return False

    #Check for upper case letter in password
    elif not any(upper.isupper() for upper in password):

        #Display error message
        print("\u274C Password Not Valid!")

        #Return False
        return False

    #If none of the above are True
    else:

        #Return True
        return True



#Create the set student ID function
def setStudentId(students):

    #Set student ID to starting value
    studentId = 700300001

    #Loop to validate until unique ID is found    
    while True:

        #Check if student ID already exists
        if str(studentId) in students:

            #Increment student ID by 1
            studentId += 1

        #If above is not true
        else:

            #Return student ID
            return str(studentId)



#Create the set name function
def setName(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a student name
        name = input("Please Enter Student Name (Firstname Lastname): ")

        #Split firstname and lastname using split method to create list
        nameSplit = name.split()

        #Check if namesplit contains two names 
        if len(nameSplit) < 2:

            #Display error message
            print("\u274C Invalid Student Name")

        #If none of the above are true
        else:

            #Set firstname to name split list index of 0
            firstname = nameSplit[0]

            #Set lastname to name split list index of 1
            lastname = nameSplit[1]
            
            #Check if firstname and lastname are capitalized 
            if not (firstname.istitle() and lastname.istitle()):  

                #Display error message
                print("\u274C Invalid Student Name")

            #Check if firstname and lastname are less than 2 letters 
            elif len(firstname) < 2 or len(lastname) < 2:

                #Display error message
                print("\u274C Invalid Student Name")

            #Check if firstname and lastname are alphabetic
            elif not (firstname.isalpha() and lastname.isalpha()):

                #Display error message
                print("\u274C Invalid Student Name")

            #If none of the above are true
            else:

                #Return student name
                return name



#Create the set age function
def setAge(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter age
        age = int(input("Please Enter Student's Age: "))

        #Validate age is between 0-100
        if age < 0 or age > 100:

            #Display Error Message
            print("\u274C Invalid Student Age")

        #If none of the above are true
        else:
            
            #Return age
            return age



#Create the set gender function
def setGender(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a major
        gender = input("Please Enter Student's Gender: ").upper()

        #Validate gender is M, F, or O
        if gender == 'M' or gender == 'F' or gender == 'O':

            #Return gender
            return gender

        #If none of the above are true
        else:

            #Display Error Message
            print("\u274C Invalid Student Gender")

    

#Create the set major function
def setMajor(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a major
        major = input("Please Enter Student's Major: ").upper()

        #Return major
        return major



#Create the set phone number function
def setPhoneNumber(students):

    #Loop to validate until correct entry is made    
    while True:

        #Prompt the user to enter a phone number
        phone = input("Please Enter Student's Phone: ")
        
        #Check if phone number is 12 characters 
        if len(phone) != 12:  

            #Display error message
            print("\u274C Invalid Phone Number")

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



#Create the custom input function
def customInput(currentValue, message, step):
        
    #Loop to validate until correct entry is made for age  
    while step == 1:

        #Prompt the user to input new value or hit enter to keep current value
        age = str(input(f"{message} (press enter without modification): "))

        #If new value is empty
        if age == "":

            #Return current value
            return currentValue

        #If condition above is not true
        else:

            #Convert age to integer
            age = int(age)

            #Validate age is between 0-100
            if age < 0 or age > 100:

                #Display Error Message
                print("\u274C Invalid Student Age")

            #If none of the above are true
            else:
                
                #Return age
                return age

    #Loop to validate until correct entry is made for major  
    while step ==  2:

        #Prompt the user to enter a major
        major = input(f"{message} (press enter without modification): ").upper()

        #If new value is empty
        if major == "":

            #Return current value
            return currentValue

        #If condition above is not true
        else:

            #Return major
            return major

    #Loop to validate until correct entry is made for phone number   
    while step == 3:

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

