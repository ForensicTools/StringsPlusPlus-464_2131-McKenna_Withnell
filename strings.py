#!/usr/bin/python
#StringsPP 
#Claire McKenna and Ben Withnell

import sys
import string
import re

#define input file as ifile
ifile=''

#get total number of arguments
total = len(sys.argv)

#test for incorrect usage, exit
if total != 2:
        print ("Usage: %s filename" % sys.argv[0])
        sys.exit(2)

#define input file
ifile = sys.argv[1]

#Function to extract readable ascii strings with greater than four characters from a file
def strings(filename, min=4):
        #Open filename (which will be passed as cli arg)
    with open(filename, "rb") as f:
        print f.name
        result = ''
        for c in f.read():
            if c in string.printable:
                result += c
                continue
        if len(result) >= min:
            yield result
            result = ""
#Store all the strings found in file in a list. Filename will be from cli arg eventually
sl = list(strings(ifile))
#Loop through each value in the list sl
for x in sl:
    #Compile IP regex into an object
    #TODO: Make "findall" work with IP addresses as well. Right now it's not properly detecting
    ip = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
    #Use the regex for md5s to find all the MD5s in x
    #TODO: Addin more regexes
    md5 = re.findall(r"([a-fA-F\d]{32})", x)
    #Print all the matching MD5s
    #TODO: Only print md5 if array !=0
    print md5
    #Seach X for matches to the IP regex
    match = ip.search(x)
    #If a match is found, print the match
    if match:
        print match.group()
    