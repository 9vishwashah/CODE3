l = []
num = int(input("number of elements you want to enter in list: "))
for i in range(1, num + 1):
	a= int(input(f"{i}st element: ")
	l.append(a)
list2 = list(set(l))
list2.sort()
print("Second largest element is:", list2[-2])
