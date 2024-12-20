#Dylan Forck
#Description: Baby name popularity ranking




#Create the name rank function
def nameRank(year, gender, name):

    #Create filename varaible
    filename = f"babynameranking{year}.txt"

    #Open the file in read mode
    file = open(filename, 'r')

    #For loop to iterate each line in the file
    for line in file:

        #Create line split list using split method
        lineSplit = line.split()

        #Rank is the first column
        rank = lineSplit[0]

        #Boy name is the second column
        boyName = lineSplit[1]

        #Girl name is the fourth column
        girlName = lineSplit[3]

        #Condition for matching boy name in list
        if boyName == name and gender.upper() == 'M':

            #Display the boy name ranking
            print(f"Boy name {boyName} is ranked #{rank} in year {year}")

            #Close the file
            file.close()

            #Exit the function
            return

        #Condition for matching girl name in list
        elif girlName == name and gender.upper() == 'F':

            #Display the girl name ranking
            print(f"Girl name {girlName} is ranked #{rank} in year {year}")

            #Close the file
            file.close()
            
            #Exit the function
            return

    #If check for gender equal to M
    if gender.upper() == 'M':

        #Display the name was not ranked for the given year
        print(f"Boy name {name} is not ranked in year {year}")

    #Else if check for gender equal to F
    elif gender.upper() == 'F':

        #Display the name was not ranked for the given year
        print(f"Girl name {name} is not ranked in year {year}")

    #Close the file
    file.close()
    
#Create the main function
def main():

    #Ask user to input the year
    year = input("Enter the year: ")

    #Ask user to input the gender
    gender = input("Enter the gender: ")

    #Ask user to input the name
    name = input("Enter the name: ")

    #Invoke the name rank function
    nameRank(year, gender, name)

#Invoke the main function
main()
