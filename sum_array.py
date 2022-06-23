def sum(arr):
  sum=0
  for i in arr:
    sum = sum + i
    return(sum)
arr=[]
arr=[2,4,6,9]
n=len(arr)
ans=sum(arr)
print('sum of the array is',ans)
