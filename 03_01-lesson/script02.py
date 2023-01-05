"""
Insertion Sort
"""

# Functions

def insertion_sort(nums):
    nums = list(nums)

    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1

        while j >= 0 and nums[j] > cur:
            j -= 1

        nums.insert(j+1, cur)

    return nums


# Main

if __name__ == '__main__':
    nums = [4, 2, 6, 3, 4, 6, 2, 1]
    print(insertion_sort(nums))
