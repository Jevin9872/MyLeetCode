from typing import List

#合并两个有序数组88
#——————》寻找两个有序数组的中位数
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = 0 #交换用
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] <= nums2[j] and nums1[i] != 0):
                    continue
                else:
                    tmp = nums1[i]
                    nums1[i] = nums2[j]
                    nums2[j] = tmp


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
S = Solution()
S.merge(nums1,m,nums2,n)
print(nums1)