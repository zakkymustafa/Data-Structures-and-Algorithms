# Project Euler
#3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factors(n):
	results = []
	i = 2
	while i*i <= n:
		(n, _results) = check_factor(n, i)
		results += _results
		i += 1
	if (n > 1):
		results += [n]
	results.sort()
	return results[-1]

def check_factor(n, i):
    results = []

    (q, r) = divmod(n, i)
    while r == 0:
        results.append(i)
        n = q
        (q, r) = divmod(n, i)

    return n, results

if __name__ == '__main__':
	print(largest_prime_factors(600851475143))
  	