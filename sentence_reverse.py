a = input("Enter the Sentence:\n")
s = a.split()[::-1]
l = []
for i in s:
	l.append(i)
print(" ".join(l))
