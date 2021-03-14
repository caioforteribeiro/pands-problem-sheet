#Program that reads a txt file and returns the number of e's it contains
#Author: Caio Forte Ribeiro

#sys module to access arguments from the command line
import sys

#filename is the second argument (index[1]) in the command line
#first argument is the name of the program (index[0])
filename = sys.argv[1]

#opens te file in read mode
with open(filename, "rt") as f:
    content = f.read()

#as 'content' is a str, we can use the count() method
#to check for occurences of 'e'
print(content.count("e"))