from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    target_1 = 0
    target_2 = 0
    done = 0
    for n in range(len(nums)):
        for i in range(1,len(nums)):
            if(nums[n]+nums[i] == target):
                target_1 = n
                target_2 = i
                done = 1
                break
        if(done == 1):
            break
    
    result = []
    result.append(target_1)
    result.append(target_2)
    return result

twoSum([3,2,4], 7)