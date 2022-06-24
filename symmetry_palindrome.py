a = input("Enter the Word:\n")
half = int(len(a) / 2)
if len(a) % 2 == 0: 
	s1 = a[:half]
	s2 = a[half:]
else: # odd
	s1 = a[:half]
	s2 = a[half+1:]
if s1 == s2:
	print(a, 'string is symmertical')
else:
	print(a, 'string is not symmertical')
if s1 == s2[::-1]:
	print(a, 'string is palindrome')
else:
	print(a, 'string is not palindrome')
