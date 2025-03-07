"""
TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

from typing import List


class Solution:
    """
    Time Complexity: O(n′2)
    Space Complexity : O (1) stores only 2 indices
    """

    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    """
       Time Complexity: O(n)
       Space Complexity : O (n) might store n indices
       
       Example:
       nums = [2, 7, 11, 15], target = 9

        Step 1: num = 2, i = 0
            complement = 9 - 2 = 7
            map = {2: 0}
        
        Step 2: num = 7, i = 1
            complement = 9 - 7 = 2
            2 exists in map! Return [map[2], 1] = [0, 1]
    """

    def twoSum_hastTable(self, nums: List[int], target: int) -> List[int]:
        num_map_dict = {}
        for i, n in enumerate(nums):
            complement = target - n

            if complement in num_map_dict:
                return [num_map_dict[complement], i]

            num_map_dict[n] = i

        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum_bruteforce(nums, target)
    print("result:", result)

    result1 = solution.twoSum_hastTable(nums, target)
    print("result1", result1)
