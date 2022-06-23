l = []
num = int(input("number of elements you want to enter in list: "))
for i in range(1, num + 1):
	a= int(input("{0}st element: ".format(i)))
	l.append(a)
print("Positive Numbers from {0} to {1} are:".format(1,i))
for n in l:
  if (n >= 0):
   print(n, end = " ")
 
