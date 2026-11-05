from typing import List

# 不要修改这个函数 sat()    do not modify this function
def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    """
    Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9.
    
    """
    # TODO: 从下一行开始写你的代码 your implementation here
    result = []
    for i in range(1, 10):      # i = 1, 2, ..., 9  (0 出现 0 次，所以不放 0)
        result += [i] * i       # 数字 i 重复 i 次
    return result  # 返回一个列表 return a list


print(sat(sol()))
