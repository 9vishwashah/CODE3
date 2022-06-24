a = input("Enter a paragraph:\n")
print("The original paragraph is : " + str(a))
b = {key: a.count(key) for key in a.split()}
print("The words frequency : " + str(b))
