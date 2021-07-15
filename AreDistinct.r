## "R" language port of the Python AreDistinct library file.

# load hash package
library(hash)

theFiles <- function(){ # need a function to get data from the files.
  
  setwd("~/myProjects/Internship") # Set working directory to source file location
  
  filesExist <- FALSE # loop control
  
  while(filesExist == FALSE){ # while control is False try to get data from users file into a list
    
    cat("\n")
    fileUsed1 <- readline(prompt = "Please enter the filename of the first file you wish to compare: ") # prompt user for first file they wish to work with
    cat("\n")
    
    if (file.exists(fileUsed1)){
      
      listOne <- scan(fileUsed1, what = integer(), sep="\n") # Add the data from the file to list one as integers
      
      fileUsed2 <- readline(prompt = "Please enter the filename of the second file you wish to compare: ") # prompt user for second file they wish to work with
      cat("\n")
      
      if (file.exists(fileUsed2)){
        
        listTwo <- scan(fileUsed2, what = integer(), sep="\n") # Add the data from the file to list two as integers
        
        ourList <- list("firstList" = listOne, "secondList" = listTwo) # create a single list  we can return from our two lists
        
        # check the length and max mins are the same as the first file / if so get out of the loop and return the list
        if ((length(ourList$firstList) == length(ourList$secondList)) && (max(ourList$firstList) == max(ourList$secondList)) && (min(ourList$firstList) == min(ourList$secondList))){
          filesExist <- TRUE
          return(ourList)
        }
        else{ # advise user the files are incompatible
          
          cat(sprintf("The structure of the chosen files are incompatible: '%s', '%s'.\n", fileUsed1, fileUsed2))
          readline(prompt = "Please press enter to try again!")
        }
      }
      # else draw attention to the missing file and advise to try again
      else{
        cat(sprintf("Unable to locate the file: '%s'. \nEnsure all files are in the working directory, and try again.", fileUsed2))
        readline(prompt = "Please press enter to continue.")
      }
    }   
    # else draw attention to the missing file and advise to try again
    else{
      cat(sprintf("Unable to locate the file: '%s'. \nEnsure all files are in the proper directory, and try again.", fileUsed1))
      readline(prompt = "Please press enter to continue.")
    }
  }
}

ourOutcome <- function(){
  
  outcome <- distinct() # Call the distinct function
  
  if (outcome){
    cat(sprintf("'%s' - The two files are distinct", outcome)) # display the results to the user
    cat("\n")
  }
  else{
    cat(sprintf("'%s' - The two files are the same", outcome)) # display the results to the user
    cat("\n")
  }
  return(outcome)
}

distinct <- function(){ # need a function that processes the data
  
  # call theFiles function
  myList <- theFiles()
  
  # get the proper values from the two lists into a data structure similar to Python Dictionary where only
  # the last values examined count as key value pairs.
  # it appears I can create this functionality by getting my unique values into a data frame
  # and then using the R hash package written by "Christopher Brown" (From everything I've been learning though,
  # attempting to write "R" code by simulating what you have done in Python is considered bad practice.)
  
  ourZipedList = data.frame(k = myList$firstList, v = myList$secondList)
  
  ourDict <- hash(keys = ourZipedList$k, values= ourZipedList$v) # We get our dictionary functionality from the hash library
  
  ourValue <- 1000000 # variable to help determine if dictionary value has been checked (set to an arbitrary value)
  
  i <- 1 # variable used to examine our second list
  
  while (i < length(myList$firstList)){
    
    x <- (myList$firstList[[i]]) # x equals the i'th value of our first list
    
    if (x == ourValue){ # check if key has already been looked at
      
      i <- (i + 1) # increment i by 1
      next # move iterator forward to skip value
    }
    else{
      
      j <- as.character(x) # cast x integer to char as j
      
      ourValue <- ourDict[[j]] # get the value of x from the dictionary (hash)
      
      outcome <- (myList$secondList[[i]] != ourValue) # get Boolean test of condition for result
      
      if (outcome){ # if outcome equals true return it
        
        return(outcome)
      }
      else{
        i = (i + 1) # increment i
      }
    }
  }
  return(outcome)
}

