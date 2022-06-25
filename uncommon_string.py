def res(a, b):
	n = [i for i in "".join(b).split() if i not in "".join(a).split()]
	return n
a = input("Enter the first sentence:\n")
b = input("Enter the second sentence:\n")
print(res(a, b))
