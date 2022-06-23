a = int(input("Enter the start of range: "))
b = int(input("Enter the end of range: "))
print("Odd Numbers from {0} to {1} are:".format(a,b))
for n in range(a, b + 1):
	if n % 2 != 0:
		print(n, end = " ")
    

