# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    a.append(i)
                    a.append(j)
        return a
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))  # Output: [0, 1]
    # print(s.twoSum([3,2,4], 6))      # Output: [1, 2]
    # print(s.twoSum([3,3], 6))        # Output: [0, 1]