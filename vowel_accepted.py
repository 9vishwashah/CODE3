import re
a = input("Enter the word:\n")
c = re.compile('[^aeiouAEIOU]')
if(len(c.findall(a))):
	print("Not Accepted") 
else:
	print("Accepted") 
