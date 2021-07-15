#import needed libraries
import os

def mySolution(): # begins the function
    
    # bring the vectors into lists
    listOne = []
    listTwo = []

    # set the proper working directory
    os.chdir(r'ourFiles')

    # Ask user to input the two files they wish to work with ensuring they are same length and have same max/mins
    same = False
    while same == False:
            print("\n")
            fileUsed1 = input("Please enter the filename of the first file you wish to compare: ")
            print("\n")
            fileUsed2 = input("please enter the filename of the second file you wish to compare: ")
            print("\n")

            # Add the data from the files to the 2 lists as integers
            tempFile = open(fileUsed1, "r")
            for line in tempFile:
                    listOne = listOne.append(int(line.strip('\n')))
                    tempFile.close

            tempFile = open(fileUsed2, "r")
            for line in tempFile:
                    listTwo = listTwo.append(int(line.strip('\n')))
                    tempFile.close

            if len(listOne) == len(listTwo):
                    
                    # check to ensure the min and max of both lists are the same
                    if min(listOne) == min(listTwo) and max(listOne) == max(listTwo):

                        same = True

                    else:
                            print("The minimum/maximum values found in each of the files indicate an incorrect file choice. Please Try Again!!!")
                            print("\n")
                            same = False
            else:
                    print("The length of the files indicate an incorrect file choice. Please Try Again!!!")
                    print("\n")
                    listOne.clear()
                    listTwo.clear()
                    same = False

    # create a dictionary which uses only the unique values found in the two lists for keys
    ourDict = dict(zip(listOne, listTwo))

    # using our dictionary and the two lists test for sameness 
    testing = True
    distinct = False
    i = 0
    while (testing == True) & (i < (len(listOne) - 1)):
        for x in listOne:
            
            # get the value of x from the dictionary
            ourValue = ourDict.get(x)
            
            # if the value found at the i'th location of list 2 does not equal the value of the x key in our dictionary 
            if listTwo[i] != ourValue:

                # distinct equals true and testing equals False
                distinct = True
                testing = False
                i = (i + 1) # iterator goes up by 1

                # else I must succeed in reaching the end of file and the two files are the same
            else:
                i = (i + 1) # iterator moves up by 1

    # display the proper results to the user
    if (distinct == True):
        print('%s' % distinct + " - The two files are distinct")
    else:
        print('%s'  % distinct + " - The two files are the same")
    print("\n") 

def main():

    # run fileComparer
    mySolution()

# Calls the main function which runs our program 
main()

#This ensures the potential flyout problem in command prompt won't be an issue.
input("Please press enter or return to quit the program.")
 