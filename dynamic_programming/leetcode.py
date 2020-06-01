# coding: utf-8
# @Author: hao.jiang
# @email: jianghao1@pcitech.com
# @time: 2020/04/13 16:05
# @Software: vscode

# region 1024  动态规划
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。

# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

#  

# 示例 1：

# 输入：2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。

# 示例 2：

# 输入：3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
# 提示:  1 <= N <= 1000
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/divisor-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion
import timeit

class Solution1024:
    def __init__(self):
        self.dp = {}

    def divisorGame(self, N: int) -> bool:
        if N == 2:
            return True
        if N == 3:
            return False
        if N in self.dp:
            return self.dp[N]

        for i in range(1, N // 2):
            if N % i != 0:
                continue
            # print(f'write {i}')
            result = not self.divisorGame(N - i)
            if result:
                self.dp[N] = True
                return result
            else:
                continue
        self.dp[N] = False
        return False


# region 53 动态规划
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution53:
    def __init__(self):
        self.dp = {}

    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


# s = Solution53()
# print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(s.maxSubArray([-2, -1]))


class Solution70:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        print(dp)
        return max(dp)


# s = Solution70()
# print(s.climbStairs(3))
# print(s.climbStairs(10))

# region 121
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

# 注意：你不能在买入股票前卖出股票。

#  

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution121:
    def maxProfit(self, prices: list) -> int:
        dp = [0] * len(prices)
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)

        print(min_price)

# region 198 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:

# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution198:
    def rob(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        print(dp)
        return max(dp) 

# s = Solution198()
# print(s.rob([1,3,1,3,100]))

# region 746
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

# 示例 1:

# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  示例 2:

# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 注意：

# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution746:
    def minCostClimbingStairs(self, cost: list) -> int:
        cost.append(0)  # leetcode 的需求是: 最后一步不消耗体能.
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return cost[1]

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return dp[-1]

# s = Solution746()
# print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(s.minCostClimbingStairs([0, 0, 0, 1]))


# region 303

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:

# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/range-sum-query-immutable
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class NumArray303:

    def __init__(self, nums: list):
        self.nums = nums
        self.nums_dict = {}
        for i in range(len(nums)):
            if i == 0:
                self.nums_dict[0] = nums[0]
                continue
            self.nums_dict[i] = self.nums_dict[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums_dict[j]
        return self.nums_dict[j] - self.nums_dict[i-1]

# n = NumArray303([-2, 0, 3, -5, 2, -1])
# print(n.sumRange(0, 2))
# print(n.sumRange(2, 5))
# print(n.sumRange(0, 5))


# region 392
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

# 示例 1:
# s = "abc", t = "ahbgdc"

# 返回 true.

# 示例 2:
# s = "axc", t = "ahbgdc"

# 返回 false.

# 后续挑战 :

# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/is-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# endregion

class Solution392:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            if s in t:
                return True
            else:
                return False
        tmp = t.find(s[0])
        if  tmp>= 0:
            
            return self.isSubsequence(s[1:], t[tmp:][1:])
        else:
            return False

""
""

# s = Solution392()
# print(s.isSubsequence(s = "axc", t = "ahbgdc"))
# print(s.isSubsequence(s = "leeeeetcode", t= "sfdd"))            


# 面试题42. 连续子数组的最大和
# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 
# 要求时间复杂度为O(n)。

#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution42:
    def maxSubArray(self, nums: list) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] += max(nums[i - 1], 0)
        # return max(nums)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max([nums[0], sum(nums), nums[1]])
        all_dp = [nums[0], max(nums[1], sum(nums[:2]))]
        for value in nums[2:]:
            if all_dp[-1] < 0:
                all_dp.append(value)
            else:
                tmp = all_dp[-1] + value
                all_dp.append(tmp)
            
        return max(all_dp)

# s = Solution42()
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(s.maxSubArray([-1, -2]))
# print(s.maxSubArray([-2, 1]))
# print(s.maxSubArray([1, 2]))
# print(s.maxSubArray([1,2,-1,-2,2,1,-2,1]))

# 1010. 总持续时间可被 60 整除的歌曲
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

# 示例 1：
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 示例 2：

# 输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
 

# 提示：

# 1 <= time.length <= 60000
# 1 <= time[i] <= 500


class Solution1010:
    def numPairsDivisibleBy60(self, time: list) -> int:
        # 最傻办法;
        count = 0
        time = [i%60 for i in time]
        for index, i in enumerate(time[:]):
            if i == 0:
                count += time[index+1:].count(0)
            else:
                count += time[index+1:].count(60-i)
        return count

    def numPairsDivisibleBy60_1(self, time: list) -> int:
        # 动态规划的思路
        if len(time) <= 1:
            return 0  # 确保至少有两组数才开始计算

        count = 0
        remainder_map = {}
        for i in time:
            rem = i % 60
            count += remainder_map.get((60-rem)%60, 0)

            if rem in remainder_map:
                remainder_map[rem] += 1
            else:
                remainder_map[rem] = 1

        return count
    
# s = Solution1010()
# print(s.numPairsDivisibleBy60_1([30,20,150,100,40]))
# print(s.numPairsDivisibleBy60_1([60,60,60]))

# 1029. 两地调度
# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

 

# 示例：

# 输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。

# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
 

# 提示：

# 1 <= costs.length <= 100
# costs.length 为偶数
# 1 <= costs[i][0], costs[i][1] <= 1000

class Solution1029:
    # 贪心算法, 每两个两个费用都是最低
    def twoCitySchedCost(self, costs: list) -> int:
        cash = 0

# 给定一个单词，你需要判断单词的大写使用是否正确。

# 我们定义，在以下情况时，单词的大写用法是正确的：

# 全部字母都是大写，比如"USA"。
# 单词中所有字母都不是大写，比如"leetcode"。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
# 否则，我们定义这个单词没有正确使用大写字母。

# 示例 1:

# 输入: "USA"
# 输出: True
# 示例 2:

# 输入: "FlaG"
# 输出: False
# 注意: 输入是由大写和小写拉丁字母组成的非空单词

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/detect-capital
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution520:
    def detectCapitalUse(self, word: str) -> bool:
        ""
        # 全部大写, [ord(i) - 90] 都会 <= 0
        # 全部小写, [ord(i) - 97] 都会 >= 0
        # 首字母大写,其余小写 word[1:] ==> ord(i) - 97 都会 >= 0
        if len(word) <= 1:
            return True
        if all([(ord(i) - 97)>=0 for i in word[1:]]):
            return True
        if all([(ord(i) - 90)<=0 for i in word]):
            return True
        return False

# s = Solution520()
# print(s.detectCapitalUse('ABD'))
# print(s.detectCapitalUse('abd'))
# print(s.detectCapitalUse('Abd'))
# print(s.detectCapitalUse('AbD'))
# print(s.detectCapitalUse('bD'))

import functools
# throw egg

x = {}

# functools.lru_cache(maxsize=99999)  # 没有起到作用?
def throw_eggs(maxLevel, numberOfEgg):
    res = float("INF")
    if maxLevel == 0:
        return 0
    if numberOfEgg == 1:
        return maxLevel

    if (maxLevel, numberOfEgg) in x:
        return x[(maxLevel, numberOfEgg)]
    
    for i in range(1, maxLevel+1):
        res = min(res, 
        max(throw_eggs(i-1, numberOfEgg-1), throw_eggs(maxLevel-i, numberOfEgg)) + 1
        )
    x[(maxLevel, numberOfEgg)] = res
    return res
    
# print(throw_eggs(20, 4))
