from sys import stdin
read_to_int_arr = lambda: map(int, stdin.readline().split())

def two_pointer(target, nums):
    N = len(nums)
    lo, hi = 0, 0
    count = 0
    total = 0

    while N > hi:
        if target > total:
            total += nums[hi]
            hi += 1
        else:
            total -= nums[lo]
            lo += 1

        if target == total:
            count += 1

    while target < total:
        total -= nums[lo]
        lo += 1

        if target == total:
            count += 1

    return count

def init():
    N, M = read_to_int_arr()
    nums = list(read_to_int_arr())
    return N, M, nums

def main():
    _, target, nums = init()
    res = two_pointer(target, nums)
    print(res)

if __name__ == '__main__':
    main()

'''
10 5
1 2 3 4 2 5 3 1 1 2
:3

4 2
1 1 1 1
:3

6 13
2 3 5 7 11 13
:1


2 3
1 3
:1
'''
# two_pointer(3,[1,3])
# two_pointer(13,[2,3,5,7,11,13])
# two_pointer(5,[1, 2, 3, 4, 2, 5, 3, 1, 1, 2])
# two_pointer(2,[1,1,1,1])
# two_pointer(2,[3,1,1,1])
