from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        #enumerate函数的使用：将可遍历数据对象组合成索引序列，同时出现数据和数组下标，一般用在for循环中
        #先把数组拆成下标位置和数值位置
        #
        for index, num in enumerate(nums):
            if target - num in tmp:
                return [tmp[target - num], index]
            tmp[num] = index

nums = [1,5,6,9,7]
target = 10
S = Solution()
print(S.twoSum(nums,target))
