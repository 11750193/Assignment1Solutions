from typing import List

# 不要修改这个函数 sat()    do not modify this function
def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    """
    Find a list of one hundred integers between 0 and 999 which all differ by at least ten from one another.
    返回一个包括100个整数的列表，（1）整数要在0到999之间（包含0和999）；（2）任意两个数最少相差10
    """
    # TODO: 从下一行开始写你的代码 your implementation here
    a=[]
    for i in range(100):
        a.append(i*10)
    return a # 返回一个列表 return a list


print(sat(sol()))
