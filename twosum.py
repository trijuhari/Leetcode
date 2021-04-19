nums = [2,7,11,15]
target = 26

def twosum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target  - v 
        if remaining in seen:
            return [seen[remaining],i]
        seen[v] = i
    return[]

print(twosum(nums, target))