from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # List to store results
    result = []
    pair = []
    # Dictionary to store the difference and its index
    index_map = {}
    # Loop for each element
    for i, n in enumerate(nums):
        # Difference which needs to be checked
        difference = target - n
        if difference in index_map:
            result.append([index_map[difference],i])
            pair.append([nums[index_map[difference]], n])

        else:
            index_map[n] = i
    return result,pair

print(twoSum([2,7,11,15,4,5],9))