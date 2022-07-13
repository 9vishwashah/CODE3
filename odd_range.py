a = int(input("Enter the start of range: "))
b = int(input("Enter the end of range: "))
print(f"Odd Numbers from {a} to {b} are:")
for n in range(a, b + 1):
	if n % 2 != 0:
		print(n, end = " ")
    

