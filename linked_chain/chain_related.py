# coding: utf8
# @Author       : danny.jiang


# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
#
# 注意：本题相对原题稍作改动
#
# 示例：
#
# 输入： 1->2->3->4->5 和 k = 2
# 输出： 4
# 说明：
#
# 给定的 k 保证是有效的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.node import *


class Solution:
    def __init__(self):
        self.header = None
        self.total = None

    def bestAnswer(self, k: int) -> int:
        # 快慢指针的标准做法.
        fastP = self.header
        slowP = self.header
        for i in range(0, k - 1):
            fastP = fastP.nextNode

        while True:
            if fastP.nextNode == None:
                print(slowP.value)
                return slowP.value
            else:
                fastP = fastP.nextNode
                slowP = slowP.nextNode

    def kthToLast(self, k: int) -> int:
        # 不好的实践.
        cur = self.header
        for i in range(0, self.total - k + 1):
            if i == self.total - k:
                pass
            else:
                cur = cur.nextNode

        print(cur.value)
        return cur.value

    def generateChain(self):
        header = None
        father = None
        total = 0
        for i in range(0, 100):
            total += 1
            if i == 0:
                header = SinglyNode()
                header.value = i
            else:
                node = SinglyNode()
                node.value = i
            if not father:
                father = header
            else:
                father.nextNode = node
                father = node

        self.header = header
        self.total = total


#
# s = Solution()
# s.generateChain()
# s.kthToLast(9)
# s.kthToLast(1)
# s.kthToLast(2)
# s.bestAnswer(9)
# s.bestAnswer(1)
# s.bestAnswer(2)

# 快慢指针,
# 反转链表,
# 哨兵节点,


# 21 合并两个有序链表
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution21:
    def mergeTwoListsReCursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            h = l1
            h.next = self.mergeTwoListsReCursion(l1.next, l2)
        else:
            h = l2
            h.next = self.mergeTwoListsReCursion(l1, l2.next)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 确保pointOne是小数开始，pointTwo是大数开始
        # 蛮力解法
        # 更优雅的方式是递归解法
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            pointOne, pointTwo = l1, l2
        else:
            pointOne, pointTwo = l2, l1

        toReturn = pointOne  # 哨兵， 用于最终函数的返回

        while True:
            if pointTwo is None:
                break

            if pointOne.next == None:
                pointOne.next = pointTwo
                break

            valueOne = pointOne.val
            valueTwo = pointTwo.val

            if valueOne <= valueTwo:
                if pointOne.next.val < valueTwo:
                    pointOne = pointOne.next
                    continue
                else:
                    tmp = pointOne.next
                    tmp2 = pointTwo.next
                    pointOne.next = pointTwo
                    pointOne.next.next = tmp
                    pointTwo = tmp2
                    continue

        return toReturn


# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
#
# 请你返回该链表所表示数字的 十进制值 。
# 输入：head = [1,0,1]
# 输出：5
# 解释：二进制数 (101) 转化为十进制数 (5)

class Solution1290:
    def getDecimalValue(self, head: ListNode) -> int:
        """很简单的逻辑，没什么好注意的"""
        # golang版 双百
        # /**
        #  * Definition for singly-linked list.
        #  * type ListNode struct {
        #  *     Val int
        #  *     Next *ListNode
        #  * }
        #  */
        # func getDecimalValue(head *ListNode) int {
        #     sum := 0
        #     if head.Next == nil{
        #         return head.Val
        #     }
        #     for {
        #         sum = head.Val + sum * 2
        #         if head.Next == nil {
        #             break
        #         }
        #         head = head.Next
        #     }
        #     return sum
        # }

        if head.next is None:
            return head.val

        sum = 0

        while True:
            sum = head.val + sum * 2
            if head.next is None:
                break
            head = head.next
        return sum
