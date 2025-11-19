from typing import List
import unittest

# BEGIN: Submission section on Leedcode
class Solution:
    def median(self, nums: List[int]):
        L = len(nums)
        assert L>0
        pos = L // 2
        if L % 2 == 0:
            return (nums[pos-1] + nums[pos])/2, pos
        else:
            return nums[pos], pos
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L1 = len(nums1)
        L2 = len(nums2)
        if L1==0 and L2==0:
            return None
        elif L1==0:
            return self.median(nums2)[0]
        elif L2==0:
            return self.median(nums1)[0]
        elif L1==1 and L2==1:
            return (nums1[0] + nums2[0])/2
        # L1>1 and L2>=1 or L1>=1 and L2>1 (at least one has length >1, and none has 0 length)
        elif L1==1:
            if L2 %2 ==0:
                if nums1[0]<nums2[L2//2-1]:
                    return nums2[L2//2-1]
                elif nums1[0]>nums2[L2//2]:
                    return nums2[L2//2]
                else:
                    return nums1[0]
            else:
                if nums1[0]<nums2[L2//2-1]:
                    return (nums2[L2//2-1] + nums2[L2//2])/2
                elif nums1[0]>nums2[L2//2+1]:
                    return (nums2[L2//2+1] + nums2[L2//2])/2
                else:
                    return (nums1[0] + nums2[L2//2])/2
        elif L2==1:
            if L1 %2 ==0:
                if nums2[0]<nums1[L1//2-1]:
                    return nums1[L1//2-1]
                elif nums2[0]>nums1[L1//2]:
                    return nums1[L1//2]
                else:
                    return nums2[0]
            else:
                if nums2[0]<nums1[L1//2-1]:
                    return (nums1[L1//2-1] + nums1[L1//2])/2
                elif nums2[0]>nums1[L1//2+1]:
                    return (nums1[L1//2+1] + nums1[L1//2])/2
                else:
                    return (nums2[0] + nums1[L1//2])/2
        elif nums1[0]<=nums2[0] and nums2[-1]<=nums1[-1]:
            nums1 = nums1[1:-1]
            return self.findMedianSortedArrays(nums1, nums2)
        elif nums2[0]<=nums1[0] and nums1[-1]<=nums2[-1]:
            nums2 = nums2[1:-1]
            return self.findMedianSortedArrays(nums1, nums2)
        elif nums1[0]<=nums2[0] and nums1[-1]<=nums2[-1]:
            nums1 = nums1[1:]
            nums2 = nums2[:-1]
            return self.findMedianSortedArrays(nums1, nums2)
        elif nums1[0]>=nums2[0] and nums1[-1]>=nums2[-1]:
            nums2 = nums2[1:]
            nums1 = nums1[:-1]
            return self.findMedianSortedArrays(nums1, nums2)
        """
        # This part seems to be not necessary
        else:
            print("Passing")
            print(f"nums1= {nums1}")
            print(f"nums2= {nums2}")
            m1, pos1 = self.median(nums1)
            m2, pos2 = self.median(nums2)
            if m1==m2:
                return m1
            elif m1<m2:
                if L1<=L2:
                    nums1 = nums1[pos1:]
                    nums2 = nums2[:-pos1]
                else:
                    nums1 = nums1[pos2:]
                    nums2 = nums2[:-pos2]
                return self.findMedianSortedArrays(nums1, nums2)
            else: #m1>m2
                if L1<=L2:
                    nums1 = nums1[:-pos1]
                    nums2 = nums2[pos1:]
                else:
                    nums1 = nums1[:-pos2]
                    nums2 = nums2[pos2:]
                return self.findMedianSortedArrays(nums1, nums2)
        """
# END: Submission section on Leedcode




class TestCalculator(unittest.TestCase):
    def test_add(self):
        sol = Solution()
        nums1= [17093, 17121, 17207, 17325]
        nums2= [17093, 17132, 17161, 17189]
        self.assertEqual(sol.findMedianSortedArrays(nums1,nums2), 17146.5)

if __name__ == '__main__':
    unittest.main()

#nums1 = [1,2,6,7]
#nums2 = [3,4,5,8]
#nums1 = [1,2]
#nums2 = [-1,3]
#print(sol.findMedianSortedArrays(nums1,nums2))
