def has_33(nums):
    c = len(nums)-1
    for i in range(c): 
        if nums[i]==3 and nums[i+1]==3:
            return True
        else:
            continue
    else:
        return False

nums = [int(i) for i in input().split()] 
a = has_33(nums)
print(f"has_33({nums})   →   {a}")