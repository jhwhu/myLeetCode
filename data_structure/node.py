# coding: utf8
# @Author       : danny.jiang
# @time         : 2020/5/28 11:12 上午
# @File         : node.py
# @Software     : PyCharm

class SinglyNode:
    def __init__(self):
        self.manager = None  # 链表的管理者, 一些全局的信息存放位置.
        self.nextNode = None
        # self.preNode = None
        self.value = ''

    def getNext(self):
        return self.nextNode

    def getValue(self):
        return self.value

    def setNext(self, n):
        self.nextNode = n

    def setValue(self, v):
        self.value = v

    def setManager(self, m):
        self.manager = m


class DoubleLinkedNode:
    def __init__(self):
        self.manager = None  # 链表的管理者, 一些全局的信息存放位置.
        self.nextNode = None
        self.preNode = None
        self.value = ''

    def getNext(self):
        return self.nextNode

    def getPre(self):
        return self.preNode

    def getValue(self):
        return self.value

    def setNext(self, n):
        self.nextNode = n

    def setPre(self, n):
        self.preNode = n

    def setValue(self, v):
        self.value = v

    def setManager(self, m):
        self.manager = m


class UnorderedNodes:
    def __init__(self):
        self.header = None  # 存放链表的头
        self.length = 0  # 存放链表的长度

    def setHeader(self, n):
        self.header = n

    def insert(self, after, n):
        """n添加到after后面"""

    def remove(self, n):
        """移除node"""
