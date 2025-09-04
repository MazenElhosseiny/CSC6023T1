import random

def MCSS(a):    # Finds the sum of the subsequence with the highest integer value in the array
    largest, acc = 0, 0
    for j in range(len(a)):
        acc += a[j]     # Adds each element to a running sum
        if acc > largest:   # If running sum is larger than current value of largest
            largest = acc
        elif acc < 0:   # If the running sum value is below 0, we want to reset it to zero
            acc = 0
    return largest

def main():
    nums = []
    for i in range(1000):
        nums.append(random.randint(-500, 500)) # Creates an random array of 1000 elements with positive and negative integer values
    
    print("The array is:", nums)
    print("The sum of the subsequence is:", MCSS(nums))

main()
