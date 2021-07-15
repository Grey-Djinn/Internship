#import needed libraries
import os

def getFiles():
        
    # loop control
    filesExist = False

    # while control is False try to get data from users file into a list
    while (filesExist == False):

        print("\n")
        fileUsed1 = input("Please enter the filename of the first file you wish to compare: ")
        #fileUsed1 = "CA1.txt"
        print("\n")
        if (os.path.exists(fileUsed1)):

            # Add the data from the file to list one as integers
            listOne = ([int(line.strip()) for line in open(fileUsed1)])

            fileUsed2 = input("Please enter the filename of the second file you wish to compare: ")
            #fileUsed2 = "CA2.txt"
            print("\n")

            if (os.path.exists(fileUsed2)):

                # Add the data from the file to list two as integers
                listTwo = ([int(line.strip()) for line in open(fileUsed2)])
                    
                # check the length and max mins are the same as the first file / if so get out of the loop
                if ((len(listOne) == len(listTwo)) & (max(listOne) == max(listTwo)) & (min(listOne) == min(listTwo))):
                    filesExist = True
                    return (listOne, listTwo)
                
                else:
                    print("The structure of the chosen files are incompatible: '" + fileUsed1 + "', '" + fileUsed2 + "'.\n")
                    input("\Please press enter to try again.")

            # else draw attention to the missing file and advise to try again
            else:
                print("Unable to locate the file: '" + fileUsed2 + "'. \nEnsure all files are in the proper directory, and try again.")
                input("\nPlease press enter to continue.")

        # else draw attention to the missing file and advise to try again
        else:
            print("Unable to locate the file: '" + fileUsed1 + "'. \nEnsure all files are in the proper directory, and try again.")
            input("\nPlease press enter to continue.")                    
                    
# determine if the two lists are the same in rotational namespace
def distinct():

    # call the getFiles function
    listOne, listTwo = getFiles()

    # create a dictionary which uses only the unique values found in the two lists for keys
    ourDict = dict(zip(listOne, listTwo))

    # using our dictionary and the two lists test for sameness 
    testing = True
    distinct = False
    i = 0

    # variable to test if value in list one has already been checked set to None
    ourValue = None

    # loop through the two lists using the keys and values of our dictionary as test elements.
    for x in listOne:

        # check if value of x has already been checked and if so skip it
        if ((x != ourValue) & (testing == True)):

            # get the value of x from the dictionary
            ourValue = ourDict[x]
            
            # if the value found at the i'th location of list 2 does not equal the value of the x key in our dictionary 
            if listTwo[i] != ourValue:

                # distinct equals true and testing equals False
                distinct = True
                testing = False

            # else I must succeed in reaching the end of file and the two files are the same
            else:
                i = (i + 1) # iterator moves up by 1

        else:
            i = (i + 1) # iterator moves up by 1     
    
    # return the proper boolean value for distinct / True if the two files are distinct : False if they are the same 
    return distinct

# output the results to user if they so desire
def results():

    # get the return value of the distinct method
    outcome = distinct()

    if (outcome == True):
        print('%s' % outcome + " - The two files are distinct")
        print("\n")
    else:
        print('%s'  % outcome + " - The two files are the same")
        print("\n") 