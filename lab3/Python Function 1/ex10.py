def unique(nums):
    unique_nums = []
    b = len(nums)
    for i in range(b):
        if nums[i] not in unique_nums:
            unique_nums.append(nums[i])
    return unique_nums

nums = [int(i) for i in input().split()]
aaa = unique(nums)
print(aaa)

