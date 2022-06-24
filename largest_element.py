def largest(arr,n):
	max = arr[0]
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max
arr=[]
n=int(input("Enter Number of elements in array:\n"))
print("Enter the elements")
for i in range(0,n):
   l=int(input())
   arr.append(l)
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)
