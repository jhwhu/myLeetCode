# coding: utf8
# @Author       : danny.jiang
# @time         : 2020/5/28 10:15 上午
# @File         : stack.py
# @Software     : PyCharm

from algorithm.data_structure.stack import Stack

def calcBaseBallScore(ops: list):
    # 你现在是棒球比赛记录员。
    # 给定一个字符串列表，每个字符串可以是以下四种类型之一：
    # 1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
    # 2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
    # 3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
    # 4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。
    #
    # 每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
    # 你需要返回你在所有回合中得分的总和。
    #
    # 示例 1:
    #
    # 输入: ["5","2","C","D","+"]
    # 输出: 30
    # 解释:
    # 第1轮：你可以得到5分。总和是：5。
    # 第2轮：你可以得到2分。总和是：7。
    # 操作1：第2轮的数据无效。总和是：5。
    # 第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
    # 第4轮：你可以得到5 + 10 = 15分。总数是：30。
    # 示例 2:
    #
    # 输入: ["5","-2","4","C","D","9","+","+"]
    # 输出: 27
    # 解释:
    # 第1轮：你可以得到5分。总和是：5。
    # 第2轮：你可以得到-2分。总数是：3。
    # 第3轮：你可以得到4分。总和是：7。
    # 操作1：第3轮的数据无效。总数是：3。
    # 第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
    # 第5轮：你可以得到9分。总数是：8。
    # 第6轮：你可以得到-4 + 9 = 5分。总数是13。
    # 第7轮：你可以得到9 + 5 = 14分。总数是27。
    # 注意：
    #
    # 输入列表的大小将介于1和1000之间。
    # 列表中的每个整数都将介于-30000和30000之间。
    #
    # 来源：力扣（LeetCode）
    # 链接：https://leetcode-cn.com/problems/baseball-game
    # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    score = 0
    stk = Stack()
    stk.push(0)
    stk.push(0)
    for op in ops:
        if op == 'C':
            stk.pop()
        elif op == 'D':
            stk.push(int(stk.peek()) * 2)
        elif op == '+':
            last = stk.pop()
            levelTwo = stk.peek()
            stk.push(last)
            stk.push(last+levelTwo)
        else:
            stk.push(int(op))

    while True:
        item = stk.pop()
        if item is not None:
            score += item
        else:
            break
    print(f'score: {score}')
    return score

# calcBaseBallScore(["5","-2","4","C","D","9","+","+"])

from collections import deque


class MinStack:
    # 设计一个支持
    # push ，pop ，top
    # 操作，并能在常数时间内检索到最小元素的栈。
    #
    # push(x) —— 将元素
    # x
    # 推入栈中。
    # pop() —— 删除栈顶的元素。
    # top() —— 获取栈顶元素。
    # getMin() —— 检索栈中的最小元素。
    #  
    #
    # 示例:
    #
    # 输入：
    # ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    # [[], [-2], [0], [-3], [], [], [], []]
    #
    # 输出：
    # [null, null, null, null, -3, null, 0, -2]
    #
    # 解释：
    # MinStack
    # minStack = new
    # MinStack();
    # minStack.push(-2);
    # minStack.push(0);
    # minStack.push(-3);
    # minStack.getMin();
    # --> 返回 - 3.
    # minStack.pop();
    # minStack.top();
    # --> 返回
    # 0.
    # minStack.getMin();
    # --> 返回 - 2.
    #  
    #
    # 提示：
    #
    # pop、top
    # 和
    # getMin
    # 操作总是在
    # 非空栈
    # 上调用。
    #
    # 来源：力扣（LeetCode）
    # 链接：https: // leetcode - cn.com / problems / min - stack
    # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    def __init__(self):
        # 最好的办法是降维打击，利用链表来解决.
        """
        initialize your data structure here.
        """
        self.stk = deque(maxlen=None)
        self.minstk = deque(maxlen=None)
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.min = x if x < self.min else self.min
        self.minstk.append(self.min)

        self.stk.append(x)

    def pop(self) -> None:
        item = self.stk.pop() if len(self.stk) > 0 else None
        self.minstk.pop() if len(self.minstk) > 0 else None
        self.min = self.minstk[-1] if len(self.minstk) > 0 else float('inf')

        return item

    def top(self) -> int:
        return self.stk[-1] if len(self.stk) > 0 else None

    def getMin(self) -> int:
        if len(self.minstk) == 0:
            return 0
        return self.minstk[-1]


# m = MinStack()
# m.push(-2)
# m.push(0)
# m.push(-3)
# m.getMin()
# m.pop()
# m.pop()
# m.getMin()