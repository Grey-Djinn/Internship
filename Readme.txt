The AreDistinct Library Helper file for Python provides the user with three functions. Two of these functions are able to be called to aid
the user in determining if two files containing a list of vectors are the same in rotational namespace even though the numbering system may
be quite different.

The usefull callable functions are "distinct", and "results" Calling "distinct" will simply return the boolean value to the calling code
with nothing output to the console. Running "results" however will return the boolean value to the calling code, while also displaying
meaningfull results in the console.

If it is determined that the two files are distinct (different), then the boolean value of True is returned. If running the "results"
function the user will also see "True - The files are distinct" displayed in the console.

If it is determined that the two files are in fact the same inside of rotational namespace then the value returned is False, and if
running the "results" function  "False - The files are the same" will be output to the console. 

The AreDistinct.py source file must be run within the same directory containing the files you wish to work with. Please ensure this is the
case.

Be sure to add "import AreDistinct" to the top of your calling source file.

Calling either function previouisly mentioned will call the "getFiles" function. There is no need to run this function seperatly. The
function will ask you for the names of the two files you wish to compare. As this is simply a Library help file, propper user input is
assumed, and the file names may be case sensitive.

The function does however check to ensure both files are the same length, and have the same maximum and minimum values. Should an error
be detected here, the function will mention the problem and ask you to try agin. 

That's really all there is to using the AreDistinct helper library. How you call the code is up to you and your personal use case, but
a basic example would be:   
                            myAnswer = AreDistinct.distinct()
                            print(myAnswer)

                            which results in:
                                                True / False (depending on files)

                                     or

                            myAnswer = AreDistinct.results()

                            which results in:
                                                True - The files are distinct / False - The files are the same
                                                                                           (depending on files)

                                                though print(myAnswer)
                                                                        Would still simply display
                                                                                             True / False (depending on files) 
                            