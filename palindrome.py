def a(s):
	return s == s[::-1]
s = input("Enter the word:\n")
r = a(s)
if r:
	print("It is a Palindrome")
else:
	print("It is not a Palindrome")
