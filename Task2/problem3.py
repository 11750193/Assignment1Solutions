from typing import List

# 不要修改这个函数 sat()    do not modify this function
def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    """
    Find a permutation of [0, 1, ..., 998] such that the ith element is *not* i, for all i=0, 1, ..., 998.
    生成一个包含[0, 1, ..., 998]的排列（列表），使第 i 个元素*不是*整数 i 
    """
    # 循环左移一位：第 i 个元素为 i+1，最后一个元素为 0
    # cyclic shift by one: the i-th element is i+1, and the last element is 0
    return list(range(1, 999)) + [0]  # 返回一个列表 return a list



print(sat(sol()))
