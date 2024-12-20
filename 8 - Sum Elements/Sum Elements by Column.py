#Dylan Forck
#Description: Sum elements column by column



#Create an empty list
m = []

#Establish variables for 3 rows and 4 columns
rowIndex = 3
columnIndex = 4

#For loop user to input data for each row based on index of row
for row in range(rowIndex):

    #Add an empty new row
    m.append([])

    #Input values for each row
    value = input(f"Enter a 3-by-4 matrix row {row}: ")

    #Split values into a list for specific row index
    valueLst = [float(x) for x in value.split()]

    #Column for loop to add values to rows
    for column in range(columnIndex):

        #Append matrix indexed row with column data
        m[row].append(valueLst[column])

#Create the sum column function
def sumColumn(m, columnIndex):

    #For loop to iterate through columns
    for column in range(columnIndex):

        #Initialize sum variable at 0
        sum = 0

        #For row in range
        for row in range(len(m)):

            #Increment sum by specific index amount
            sum += m[row][column]

        #Print the result for each column
        print(f"Sum of the elements at column {column} is {sum}")

#Invoke the sum column function to display the results
sumColumn(m, columnIndex)
