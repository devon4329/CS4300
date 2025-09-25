# Task 7 - Package Management in DevEdu

import numpy as np

def calculate(input):
    average = np.mean(input)
    median = np.median(input)
    
    return average, median

if __name__ == "__main__":
    data = [3, 6, 2, 5, 19, 1]
    mean , median = calculate(data)
    print(f"Mean: {mean}, Median: {median}")
