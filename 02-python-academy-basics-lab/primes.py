import math
def primes_in_range(n=10):
	""" Finds the prime numbers in the given range by Eratosthenes method.	"""
	numbers = [1] * n
	# print("len ", len(numbers))
	# print(numbers)
	prime_numbers = []

	for p in range(2, n//2):
		i = p
		while(i < n ):
			i += p
			if i> n :
				break
			numbers[i - 2] = 0

	for i in range(n-1):
		if numbers[i] == 1 :
			prime_numbers.append(i+2)
	# print(prime_numbers)
	return prime_numbers

if __name__ ==  "__main__":

	# n = int(input("Please, enter range end"))
	n = 26 #not finished

	primes = primes_in_range(n)
	print("\nPrimes:\n", primes)
