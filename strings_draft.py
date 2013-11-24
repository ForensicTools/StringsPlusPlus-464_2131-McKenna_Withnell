#!/usr/bin/python
#StringsPP 
#Claire McKenna and Ben Withnell

import os
import sys
import string
import re
from IPy import IP
import tldextract

#define input file as ifile
ifile= [ ]

#get total number of arguments
total = len(sys.argv)

#test for incorrect usage, exit
if total < 2:
       	print ("Usage: %s filename [-d for directory]" % sys.argv[0])
       	sys.exit(2)

if total > 2:
	if sys.argv[2] == "-d":
		#collect files
		directory = sys.argv[1]
		path = r"%s" % directory
		for file in os.listdir(path):
			current_file = os.path.join(path, file)
			ifile.append(current_file) 
	else:
		print ("Usage: %s filename [-d for directory]" % sys.argv[0])
		sys.exit(2)
if total == 2:	
	#define input file
	ifile.append(sys.argv[1])

#Function to extract readable ascii strings with greater than four characters from a file
def strings(filename, min=4):
        #Open filename (which will be passed as cli arg)
    with open(filename, "rb") as f:
        result = ''
        for c in f.read():
            if c in string.printable:
                result += c
                continue
        if len(result) >= min:
            yield result
            result = ""
#Store all the strings found in file in a list. Filename will be from cli arg eventually
#sl = list(strings(ifile[0]))
matchedIPs = [ ]
privateIPs = [ ]
matchDomain = [ ]
emailAddr = [ ]

#Define and compile regular expressions
md5Regex = re.compile(r"([a-fA-F\d]{32})")
ipRegex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
domain = re.compile(r'[\w\-\.]+\.(?:com|org|biz|net|ru|info|es|in|biz|nl|cn)')
email = re.compile(r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')

#loop through each file contained in ifile			
for file in ifile:
	#Store all the strings found in file in a list. Filename will be from cli arg eventually
	sl = list(strings(file))
	matchedIPs = [ ]
	privateIPs = [ ]

	#Loop through each value in the list sl
	for x in sl:
	    #Use the regex for md5s to find all the MD5s in x
	    #TODO: Addin more regexes
	    md5 = re.findall(md5Regex, x)
	    #Seach X for all matches to the IP regex and store in the list matchedIPs
	    matchedIPs = re.findall(ipRegex, x)
	    #Extract domains from x
    	matchDomain = re.findall(domain, x) 
    	#Extract all email addresses found in x
    	emailAddr = re.findall(email, x)

	#Print filename
	fo = open(file,"r")
	
	print ("\nFile Name: %s" % fo.name)
	print "------------------------------"

	#If the md5 list is not empty, print all the items in the list
	if md5:
	    #Print the header first then each item (MD5sum) in the list md5. Prints each one on a new line
	    print "\nPossible MD5s Found:"
	    for item in md5:
	        print item
	#If the md5 list is empty, print the string below
	if not md5:
	    print "\nNo MD5s Found"

	#If matchDomain is not empty, print each item (domain) in the list on a new line. If empty, print No Domain Names Found    
	if matchDomain:
	    print "\nPossible Domain Names Found:"
	    for item in matchDomain:
	        print item
	if not matchDomain:
	    print "\nNo Domain Names Found"

	#If emailAddr is not empty, print each item (email address) in the list on a new line. If empty print message
	if emailAddr:
	    print "\nPossible Email Addresses Found:"
	    for item in emailAddr:
	        #Print only the email address instead of email, domain name
	        print item[0]
	if not emailAddr:
	    print "\nNo Email Addresses Found"
	#If the matchedIPs list is not empty, print all of the items in the list
	if matchedIPs:
	    print "\nPossible IP Addresses Found:"
	    #Print out IP address results
	    for item in matchedIPs:
	        #Use the IP module to check IP address type (PRIVATE, PUBLIC or LOOPBACK)
	        ip = IP(item)
	        #If the IP is identified as a private IP address, append the IP to the privateIPs list
	        if ip.iptype() == 'PRIVATE':
	            privateIPs.append(item)
	        #If the IP is not a private IP address, print the address as part of the IP Address section
	        else:
	            print item
	#If the matchedIPs list is empty, print the string below
	if not matchedIPs:
	    print "\nNo IP Addresses Found."
	#If any privateIP addresses were found, print them out under the Private IP Addresses header
	#Do we want to separate out the IP addresses like this, or do we want to just list them under one category and put (PRIVATE) next to each address?
	#If we did this we could even use iptype() to display the type (PUBLIC, PRIVATE or LOOPBACK) next to all IPs
	if privateIPs:
	    print "Private IP Addresses:"
	    for item in privateIPs:
	        print item

