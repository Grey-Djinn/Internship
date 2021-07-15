import os # import needed libraries

def getFiles():
        
    filesExist = 0 # loop control

    while (filesExist == 0): # while control is False try to get data from users file into a list

        print("\n")
        fileUsed1 = input("Please enter the filename of the first file you wish to compare: ")
        print("\n")
        if (os.path.exists(fileUsed1)):

            listOne = ([int(line.strip()) for line in open(fileUsed1)]) # Add the data from the file to list one as integers

            fileUsed2 = input("Please enter the filename of the second file you wish to compare: ")
            print("\n")

            if (os.path.exists(fileUsed2)):

                listTwo = ([int(line.strip()) for line in open(fileUsed2)]) # Add the data from the file to list two as integers
                    
                
                if ((len(listOne) == len(listTwo)) & (max(listOne) == max(listTwo)) & (min(listOne) == min(listTwo))): # check the length and max mins are the same as the first file / if so get out of the loop
                    return (listOne, listTwo)
                
                else:
                    print("The structure of the chosen files are incompatible: '" + fileUsed1 + "', '" + fileUsed2 + "'.\n") # explain the files are not correct
                    input("\Please press enter to try again.")

            else: # else draw attention to the missing file and advise to try again
                print("Unable to locate the file: '" + fileUsed2 + "'. \nEnsure all files are in the proper directory, and try again.")
                input("\nPlease press enter to continue.")

        else: # else draw attention to the missing file and advise to try again
            print("Unable to locate the file: '" + fileUsed1 + "'. \nEnsure all files are in the proper directory, and try again.")
            input("\nPlease press enter to continue.")                    
                    
def distinct(): # determine if the two lists are the same in rotational namespace
 
    listOne, listTwo = getFiles() # call the getFiles function

    ourDict = dict(zip(listOne, listTwo)) # create a dictionary which uses only the unique values found in the two lists for keys 
    
    i = 0 # variable used to examine list two 
    
    ourValue = 1000000 # variable to test if value in list one has already been checked (set to Arbitrary number)

    for x in listOne: # loop through the two lists using the keys and values of our dictionary as test elements.

        if (x != ourValue): # check if value of x has already been checked and if so skip it

            ourValue = ourDict[x] # get the value of x from the dictionary
            
            distinct = (listTwo[i] != ourValue) # get bool value of distinct

            if (distinct): # if distinct is known to be true break free from the loop by returning value of distinct

                return distinct
              
            else:
                i = (i + 1) # else increment i and continue

        else:
            i = (i + 1) # skip this iteration and increment i by 1    
     
    return distinct # return the proper boolean value for distinct / True if the two files are distinct : False if they are the same

def results(): # output the results to user if they so desire

    outcome = distinct() # get the return value of the distinct method

    if (outcome):
        print('%s' % outcome + " - The two files are distinct")
        print("\n")
    else:
        print('%s'  % outcome + " - The two files are the same")
        print("\n")

    return outcome 