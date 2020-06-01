# coding: utf-8
# @Author: hao.jiang
# @email: jianghao1@pcitech.com
# @time: 2020/04/13 14:10
# @Software: vscode

# 给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，
# 每种硬币的数量无限，再给一个总金额 amount，
# 问你最少需要几枚硬币凑出这个金额

dpCoins = {}


def getMinCoins(total: int, coins: list):
    if total in dpCoins:
        return dpCoins[total]

    if total == 0:
        return 0
    if total < 0:
        return -1

    res = float('INF')
    for coin in coins:
        tmp = getMinCoins(total-coin, coins)
        if tmp is None or tmp < 0:
            continue
        res_tmp = 1 + tmp
        if res is None:
            res = res_tmp
        else:
            res = min(res_tmp, res)
    dpCoins[total] = res
    print(total, f'{res}')
    return res

res = getMinCoins(103, [5])
if res is float('INF'):
    print(f'there is no solution for this situation.')
else:
    print('res is: ', res)
