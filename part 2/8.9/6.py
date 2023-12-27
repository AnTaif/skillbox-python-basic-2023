def partition(nums):
    pivot = nums[-1]
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]
    return less, equal, greater

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        less, equal, greater = partition(nums)
        return quick_sort(less) + equal + quick_sort(greater)

numbers = [4, 9, 2, 7, 5]
result = quick_sort(numbers)
print(result)
