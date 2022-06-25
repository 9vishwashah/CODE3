a=input("Enter the string:\n")
a.split()
c=0
s='[@_!#$%^&*()<>?/\|}{~:]' 
for i in range(len(a)):
	if a[i] in s:
	 c+=1
if c:
	print("string is not accepted")
else:
	print("string accepted")
