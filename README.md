StringsPlusPlus-464_2131-McKenna_Withnell
=========================================
Claire McKenna and Ben Withnell, 2013

"a powerful strings extractor/analyzer"

Strings++ is intended to pull printable strings from malware and other files such as DNS logs and parse this data to return categorized output. This could include IP addresses, domain names, hard coded HTTP headers, possibly even permutations of domains, such as goolge.com instead of google.com. These predefined patterns in data are intended to make the forensic investigation process more efficient by presenting the key information the investigator may be looking for. At the moment, investigators have to manually parse through malware strings, or design their own scripts to parse the data so our tool will hopefully make the process faster and more efficient. 
There will be no “intelligence” to this tool beyond extracting the data patterns it is set to look for. It will not look at the output and make any determination on its own as to which information is more important than other pieces. 