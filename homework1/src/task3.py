# Task 3 - Control Structures
import math

# Checking if number is pos, neg, or zero
def check_num(x):
    if x > 0:
        return "Positive"
    
    elif x < 0:
        return "Negative"

    else:
        return "Zero"

# for loop to print results of first 10 primes
def for_primes(num):
    prime_list = []
    prime_num = 2

    while len(prime_list) < num:
        is_prime = True
        for i in range (2, int(math.sqrt(prime_num)) + 1):
            if prime_num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(prime_num)
        prime_num += 1
    return prime_list        

# While loop to find the sum of all numbers from 1 to 100
def the_sum(nums):
    total = 0
    count = 1

    while count <= nums:
        total += count
        count += 1
    
    return total

if __name__ == "__main__":
    n = 10
    prime_list = for_primes(n)
    print(prime_list)
