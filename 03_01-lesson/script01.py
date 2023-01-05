"""
Bubble Sort
"""

# Functions

def bubble_sort(nums):
    nums = list(nums)

    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums


# Main

if __name__ == '__main__':
    nums = [4, 2, 6, 3, 4, 6, 2, 1]
    print(bubble_sort(nums))
