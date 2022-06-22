num=int(input("Enter the number:\n"))
if num>1:
    for i in range(2, int(num/2)+1): 
        if (num%i)==0:
          print(num,"Is not a prime number")
          break
    else:
       print(num,"Is a prime number")
else:
    print(num,"Is not a prime number")
