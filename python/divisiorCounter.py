
def numberOfDivisors(num):
	c = 0


	for i in range(1, num + 1) :
		if (num % i == 0) :
			c += 1
		
	return c

def countNumbers(n):

	c = 0

	for i in range(1, n + 1) :
		

		if (numberOfDivisors(i) == 9):
			c += 1
	return c

if __name__ == "__main__":
    n = int(input("Enter number : "))
    print(countNumbers(n))

