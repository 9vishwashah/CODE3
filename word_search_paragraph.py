def check(s2, s1):
	if (s2.count(s1) > 0):
		print("{0} Word is present in the paragraph".format(s1))
	else:
		print("{0} Word is present in the paragraph".format(s1))
s2 = input("Enter the paragraph:\n")
s1 = input("Enter a word you want to search:\n")
check(s2, s1)
