def check(s2, s1):
	if (s2.count(s1) > 0):
		print(f"{s1} Word is present in the paragraph")
	else:
		print(f"{s1} Word is present in the paragraph")
s2 = input("Enter the paragraph:\n")
s1 = input("Enter a word you want to search:\n")
check(s2, s1)
