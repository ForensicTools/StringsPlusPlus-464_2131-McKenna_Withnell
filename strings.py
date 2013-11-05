import string

#Function to extract readable ascii strings with greater than four characters from a file
def strings(filename, min=4):
	#Open filename (which will be passed as cli arg
    with open(filename, "rb") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
#Store all the strings found in file in a list. Filename will be from cli arg eventually
sl = list(strings("fileName"))
print sl