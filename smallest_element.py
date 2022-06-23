l = []
num = int(input("number of elements you want to enter in list: "))
for i in range(1, num + 1):
	a= int(input("{0}st element: ".format(i)))
	l.append(a)
print("Smallest element is:", min(l))

