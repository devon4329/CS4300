# Task 3 - Control Structures

# Checking if number is pos, neg, or zero
def check_num(x):
    if x > 0:
        return "Positive"
    
    elif x < 0:
        return "Negative"

    else:
        return "Zero"

# for loop to print results of firt 10 primes
def for_primes(N):
    primes_list = []
    start_num = 2
    for i in range(start_num, N):
        if start_num % i == 0:
            
    return True

# While loop to find the sum of all numbers from 1 to 100
def the_sum(nums):
    total = 0
    count = 1

    while count <= nums:
        total += count
        count += 1
    
    return total
