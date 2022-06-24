a = input("Enter a word:\n")
b = ""
n=int(input("Enter the position of a letter from word you want to remove:\n"))
for i in range(len(a)):
	if i != n-1:
		b = b + a[i]
print ("The original string is : " + a)
print ("The string after removal of {0} position of word: {1}".format(n,b))
