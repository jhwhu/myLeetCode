# coding: utf-8
# @Author: hao.jiang
# @email: jianghao1@pcitech.com
# @time: 2020/04/13 15:30
# @Software: vscode

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


class Solution:
    def __init__(self):
        self.dp = {1:1,2:2,3:4}
    def waysToStep(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n <= 0:
            return -1
        if n in [1, 2]:
            return n
        if n == 3:
            return 4
        
        count = 0

        for i in range(4, n):
            for step in [1, 2, 3]:
                sub_count = self.waysToStep(i-step)
                if sub_count == -1:
                    continue
                count += sub_count
        self.dp[n] = count%1000000007
        print(n, ': ', self.dp[n])
        return self.dp[n]

s = Solution()
# print(s.waysToStep(4))
# print(s.waysToStep(5))
print(s.waysToStep(900750))


# region 16.17
# 给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

# 示例：

# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = [nums[0]]
        for index, value in enumerate(nums[1:]):
            tmp = max(value, result[index] + value)
            result.append(tmp)
        
        return max(result)