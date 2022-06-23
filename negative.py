a=int(input("Enter the start range:"))
b=int(input("Enter the end range:"))
for n in range(a,b+1):
  if n<0:
    print(n,end="")
