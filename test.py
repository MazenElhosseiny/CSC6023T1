import random

def MCSS(a):
    largest, acc = 0, 0
    for j in range(len(a)):
        acc += a[j]
        if acc > largest:
            largest = acc
        elif acc < 0:
            acc = 0
    return largest

def main():
    a = [5, -1, 56, -3, -18, 22, -9]
    b = [-2, 11, -4, 13, -5, 2]
    nums = []
    for i in range(1000):
        nums.append(random.randint(-500, 500))
    
    
    print(nums)
    print(MCSS(nums))

main()
