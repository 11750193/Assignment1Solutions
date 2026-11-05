from typing import List

# 不要修改这个函数 sat()    do not modify this function
def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    """
    Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9.
    
    """
    # TODO:
    # 从下一行开始写你的代码 your implementation here
    a=[]
    for i in range(1,10):
        for j in range(1,i+1):
            a.append(i)
    return a # 返回一个列表 return a list



print(sat(sol()))
