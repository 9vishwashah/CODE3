def string_k(k, str):
	string = []
	text = str.split(" ")
	for x in text:
		if len(x) > k-1:
			string.append(x)
	return string
k =int(input("Enter the length of string:\n"))
str = input("Enter the string:\n")
print(string_k(k, str))
