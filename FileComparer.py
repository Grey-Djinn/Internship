# import needed libraries
import os
from renumberer import renumberer

def fileComparer(): # begins the main method
     
    # check if renumberer has been run, if not run it
    path = 'ourRenumberedFiles'
    renumExists = os.path.isdir(path)

    if not renumExists: # if block verifies our renumbered files folder exists or not
        renumberer() # run renumberer
    else:
        os.chdir(r'ourRenumberedFiles') # or else set directory to our renumbered files dir

    # Create two dynamic lists to hold our data from the renumbered text files
    fileList_1 = []
    fileList_2 = []

    # Ask user to input the two files they wish to work with ensuring they are same length and have same max/mins
    same = False
    while same == False:
            print("\n")
            fileUsed1 = input("Please enter the filename of the first file you wish to compare: ")
            print("\n")
            fileUsed2 = input("please enter the filename of the second file you wish to compare: ")
            print("\n")

            fileList_1 = ([int(line.strip()) for line in open(fileUsed1)]) # Add the data from the file to list one as integers

            fileList_2 = ([int(line.strip()) for line in open(fileUsed2)]) # Add the data from the file to list one as integers

            if len(fileList_1) == len(fileList_2):
                    
                    # check to ensure the min and max of both lists are the same
                    if min(fileList_1) == min(fileList_2) and max(fileList_1) == max(fileList_2):

                        same = True

                    else:
                            print("The minimum/maximum values found in each of the files indicate an incorrect file choice. Please Try Again!!!")
                            print("\n")
                            same = False
            else:
                    print("The length of the files indicate an incorrect file choice. Please Try Again!!!")
                    print("\n")
                    fileList_1.clear()
                    fileList_2.clear()
                    same = False

    result = (fileList_1 != fileList_2)
    if (result):
        print('%s' % result + " - The two files are distinct")
    else:
        print('%s'  % result + " - The two files are the same")
    print("\n")

    return result

