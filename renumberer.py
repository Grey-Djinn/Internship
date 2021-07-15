# import needed libraries
import glob
import os

def renumberer():

    # create a dynamic list to store the files original values
    theFile = []

    # create a dynamic list to store the renumbered files
    renumberedFile = []
    
    # add all .txt files into a list
    os.chdir(r'ourOriginalFiles')
    ourfiles = glob.glob('*.txt')

    # ensure a directory for our renumbered files exists - if not create one
    if not os.path.exists('../ourRenumberedFiles'):
        os.makedirs('../ourRenumberedFiles')

    # loop through the list of text files, adding their values to individual lists
    for x in ourfiles:

        # go back to original directory
        os.chdir(r'../ourOriginalFiles')
        
        # store the values in a temp file and write them to our newly created file list - close the temp file
        tempFile = open(x, "r")
        for line in tempFile:
                theFile.append(int(line.strip('\n')))
                tempFile.close

        # get the unique values from the list into their own list
        uniqueValues = []

        # Traverse the lists to get the unique values
        for i in theFile:
                if i not in uniqueValues:
                        uniqueValues.append(i)

        # create a list the same length as the uniqueValues sequentialy numbered from 1
        newValues = []
        value = 1
        for y in uniqueValues:
                newValues.append(value)
                value = (value + 1)

        # create a dictionary with the unique values as keys and the new values as simply that (values)
        file_Dict = dict(zip(uniqueValues, newValues))

        # use a for loop to Renumber the lists by creating new lists
        for k in theFile:
            valueKeys = file_Dict.get(k)
            renumberedFile.append(valueKeys) #assign keys to appropriate spot in dictionary

        # Output the values from the renumbered list to a file in the renumbered directory
        # first get the right filename and open one to write
        os.chdir(r'../ourRenumberedFiles')
        textFile = open(x, 'w')
        # loop through the renumbered list converting values to a string and writing them to a file in the renumbered directory
        for n in renumberedFile:
            textFile.write("%s" % n + "\n")
        textFile.close()

        # Clear out the lists and dictionary for the next iteration
        theFile.clear()
        renumberedFile.clear()
        file_Dict.clear()
        uniqueValues.clear()
        newValues.clear()