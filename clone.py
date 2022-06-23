def Cloning(li1):
	li_copy = list(li1)
	return li_copy
li1 = []
a=int(input("number of elements:\n"))
li1.append(a)
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
