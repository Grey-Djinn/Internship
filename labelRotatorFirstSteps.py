# Date: June 4, 2021.
# CIS 380 Internship Project
# Author: Christopher Crowley
# Organizational Mentor: Dr. Matthew Dube
# Faculty Mentor: Mark Goodridge

## We are starting out with the creation of a label rotator. This first portion of the project requires a function with the ability to analyze and compare
## the values held in the text files of the states of Idaho, Arizona, and California. Each state has three files, two of which contain the 
## identical political district map information with a different numbering scheme.
# 
## We are to start with Idaho as it is the easiest of the three, and work our way up to California which is the most difficult. We will need to take in the data,
## make our comparisons, and track which location is in each district. Once we can successfully do this for all three states, we can perform tests and code for
## efficiency.
# 
## This is the Python version of the program. Per the learning objectives Dr. Dube and I came up with, I will be attempting to create this code in the 'R' language
## asw well.

## psudo code - what this function needs to do

# 1 - take in the data into a format we can analyze

# 2 - 

# import needed libraries
import os

def main(): # begins the main method

    # Create three dynamic lists to hold our data from the state text files
    state1 = []
    state2 = []
    state3 = []

    # Create three dynamic lists to hold our renumbered values
    renumberedState1 = []
    renumberedState2 = []
    renumberedState3 = []

    # assign the directory to be used
    os.chdir(r'ourOriginalFiles')

    # Ask user to input the three files they wish to work with ensuring they are same length and have same max/mins
    same = False
    while same == False:
            print("\n")
            stateUsed1 = input("Please enter the filename of the first file you wish to compare: ")
            stateUsed2 = input("please enter the filename of the second file you wish to compare: ")
            stateUsed3 = input("please enter the filename of the third file you wish to compare: ")

            # Add the data from the files to the 3 lists as integers
            tempFile = open(stateUsed1, "r")
            for line in tempFile:
                    state1.append(int(line.strip('\n')))
                    tempFile.close

            tempFile = open(stateUsed2, "r")
            for line in tempFile:
                    state2.append(int(line.strip('\n')))
                    tempFile.close

            tempFile = open(stateUsed3, "r")
            for line in tempFile:
                    state3.append(int(line.strip('\n')))
                    tempFile.close

            length = len(state1)

            if all(len(lst) == length for lst in [state2, state3]):
                    # Get the unique values found in our lists into own lists
                    state1_Values = []
                    state2_Values = []
                    state3_Values = []

                    # Traverse the lists to get the uniqe values
                    for x in state1:
                            if x not in state1_Values:
                                    state1_Values.append(x)

                    for i in state2:
                            if i not in state2_Values:
                                    state2_Values.append(i)

                    for y in state3:
                            if y not in state3_Values:
                                    state3_Values.append(y)

                    if min(state1_Values) == min(state2_Values) and min(state2_Values) == min(state3_Values):
                            if max(state1_Values) == max(state2_Values) and max(state2_Values) == max(state3_Values):
                                    same = True
                            else:
                                    print("The maximum values found in each of the files indicate an incorrect file choice. Please Try Again!!!")
                                    print("\n")
                                    same = False

                    else:
                            print("The minimum values found in each of the files indicate an incorrect file choice. Please Try Again!!!")
                            print("\n")
                            same = False
            else:
                    print("The length of the files indicate an incorrect file choice. Please Try Again!!!")
                    print("\n")
                    state1.clear()
                    state2.clear()
                    state3.clear()
                    same = False

    # create a list the same length as the state_Values sequentialy numbered from 1
    newNumbers = []
    number = 1
    for x in state1_Values:
            newNumbers.append(number)
            number = (number + 1)

    # Create a dictionary with state_values as keys and newNumbers as values for the three states
    state1_Dict = {state1_Values[i]: newNumbers[i] for i in range(len(state1_Values))}
    state2_Dict = {state2_Values[i]: newNumbers[i] for i in range(len(state2_Values))}
    state3_Dict = {state3_Values[i]: newNumbers[i] for i in range(len(state3_Values))}

    # use a for loop to Renumber the lists by creating new lists
    for i in state1:
            # get the dictionary keys value for the state
            valueS1 = state1_Dict.get(i)
            renumberedState1.append(valueS1)

    for i in state2:
            # get the dictionary keys value for the state
            valuesS2 = state2_Dict.get(i)
            renumberedState2.append(valuesS2)

    for i in state3:
            # get the dictionary keys value for the state
            valuesS3 = state3_Dict.get(i)
            renumberedState3.append(valuesS3)

    print("------------------------------------------------------------------------------------------------")
    print("\n")

    print(renumberedState1)
    print("\n")
    print(renumberedState2)
    print("\n")
    print(renumberedState3)
    print("\n")

    print(renumberedState1 != renumberedState2)
    print(renumberedState1 != renumberedState3)
    print(renumberedState2 != renumberedState3)

# Calls the main function which runs our program 
main()

#This ensures the potential flyout problem in command prompt won't be an issue.
input("Please press enter or return to quit the program.")