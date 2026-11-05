from typing import List

# 不要修改这个函数 sat()    do not modify this function
def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    """
    Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998.
    生成一个包含[0, 1, ..., 998]的排列（列表），使第 i 个元素*不是*整数 i 
    """
    # TODO: 从下一行开始写你的代码 your implementation here
    a=[]
    for i in range(999):
        b=i+1
        c=b%999
        a.append(c)
    return a # 返回一个列表 return a list



print(sat(sol()))
