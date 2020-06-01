# coding: utf8
# @Author       : danny.jiang
# @time         : 2020/5/28 10:06 上午
# @File         : stack.py
# @Software     : PyCharm

from collections import deque


class Stack:

    def __init__(self):
        self.stk = deque(maxlen=None)

    def peek(self):
        return self.stk[-1] if len(self.stk) > 0 else None

    def peekLeft(self):
        return self.stk[0] if len(self.stk) > 0 else None

    def pop(self):
        item = self.stk.pop() if len(self.stk) > 0 else None
        return item

    def popLeft(self):
        item = self.stk.popleft() if len(self.stk) > 0 else None
        return item

    def push(self, item):
        self.stk.append(item)

    def pushLeft(self, item):
        self.stk.appendleft(item)

    def size(self):
        return len(self.stk)

    def isEmpty(self):
        return len(self.stk) == 0
