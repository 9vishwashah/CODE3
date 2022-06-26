from collections import Counter
def find_dup_char(A):
	a = Counter(A)
	for letter, count in a.items():
		if (count > 1):
			print(letter)
if __name__ == "__main__":
	A = input("Enter a String:\n")
	find_dup_char(A)
