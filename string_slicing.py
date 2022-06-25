def rotate(str1,n):
 temp = str1 + str1
 l1 = len(str1)
 l2 = len(temp)
 Lfirst = temp[n : l1+n]
 Lsecond = temp[l1-n : l2-n]
 print ("Left Rotation : ", Lfirst)
 print ("Right Rotation : ", Lsecond )
if __name__ == "__main__":
	input = 'Vishwa'
	d=2
	rotate(input,d)
