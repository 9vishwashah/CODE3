n= int(input("Enter the number:\n"))
def squaresum(n) :
	sm = 0
	for i in range(1, n+1) :
		sm = sm + (i * i)
	return sm
print(squaresum(n))

