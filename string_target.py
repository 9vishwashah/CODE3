import string
import random
import time
a = string.ascii_lowercase + string.digits +string.ascii_uppercase + ' ., !?;:'
t = input("Enter the string:\n")
b = ''.join(random.choice(a)
								for i in range(len(t)))
c = ''
res = False
iteration = 0
while res == False:
	print(b)
	c = ''
	res = True
	for i in range(len(t)):
		if b[i] != t[i]:
			res = False
			c += random.choice(a)
		else:
			c += t[i]
	iteration += 1
	b = c
	time.sleep(0.1)
print("Target matched after " +
	str(iteration) + " iterations")
