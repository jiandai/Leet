from typing import List
import unittest

'''
# version 1: time O(n^2) / space O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
'''

'''
# version 2: time O(2n) / space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(len(nums)):
            m[target - nums[i]] = i
        #print(m)
        for i in range(len(nums)):
            #print(f"process {i}")
            if nums[i] in m and m[nums[i]] != i:
                return [min(m[nums[i]], i), max(m[nums[i]], i)]
'''

# version 3: time O(n) / space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(len(nums)):
            if nums[i] in m:
                return [m[nums[i]], i] 
            m[target - nums[i]] = i


class TestSolution(unittest.TestCase):
    def test_sum(self):
        sumtest = Solution()
        self.assertEqual(sumtest.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(sumtest.twoSum([3,2,4],6), [1,2])
        self.assertEqual(sumtest.twoSum([3,3],6), [0,1])
        self.assertEqual(sumtest.twoSum([2,5,5,11],10), [1,2])
if __name__ == "__main__":
    unittest.main()
