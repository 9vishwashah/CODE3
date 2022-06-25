test_str = 'Hello my name is Vishwa Shah. I am pursuing Diploma in Ai&Ml branch in Agnel Polytechnic'
print("The original string is : " + str(test_str))
repl_dict = {'in' : 'at' }
test_list = test_str.split(' ')
res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != idx
								else val for idx, val in enumerate(test_list)])
print("The string after replacing : " + str(res))
