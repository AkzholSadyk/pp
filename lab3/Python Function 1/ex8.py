def spy_game(nums):
    b=[]
    c = len(nums)
    for i in range(c): 
        if nums[i]==0 or nums[i]==7:
            b.append(nums[i])
        else:
            continue
    if len(b)==3:
        if b == [0, 0, 7]:
            return True
        else:
            return False
    
nums = [int(i) for i in input().split()] 
a = spy_game(nums)
print(f"spy_game({nums}) --> {a}")
