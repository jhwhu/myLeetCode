# coding: utf8
# @Author       : danny.jiang
# @time         : 2020/6/3 19:21
# @File         : data_list.py
# @Software     : PyCharm

# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        # 滑块的思路。复杂度 (m-n) * n
        # 这种思路+指针，可以稍微改进时间复杂度，最好 n,最坏没变化
        # 官方的大长度情况应该是用hash值来比较。最坏时间复杂度是 m-n  ===> 滚动hash
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        if len(needle) == len(haystack):
            return 0 if needle == haystack else -1

        l = len(needle)
        cp = hash(needle)
        for i in range(len(haystack) - len(needle) + 1):
            # if haystack[i:i+l] == needle:
            if hash(haystack[i:i + l]) == cp:
                return i
        return -1


# 给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
#
# 完成所有替换操作后，请你返回这个数组。
#
#  
#
# 示例：
#
# 输入：arr = [17,18,5,4,6,1]
# 输出：[18,6,6,6,1,-1]
#
class Solution1299:
    def replaceElements(self, arr):
        arr.append(-1)
        cur_max = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = cur_max
            cur_max = max(cur_max, tmp)
        return arr[:-1]




if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(Solution1299().replaceElements(arr))
