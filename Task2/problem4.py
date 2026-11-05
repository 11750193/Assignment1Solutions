# 不要修改这个函数 sat()    do not modify this function
def sat(prod: int, n=14235764939971075543215213):
    for c in str(n):
        i = int(c)
        if i % 2 == 1:
            assert prod % i == 0
            prod //= i
    return prod == any(int(c) % 2 for c in str(n))

def sol(n=14235764939971075543215213):
    """
    Return the product of the odd digits in n, or 0 if there aren't any
    返回整数 n 各数位中奇数的乘积；如果不含奇数，返回 0
    如：n = 12345, 返回 15
    """
    # TODO: 从下一行开始写你的代码 your implementation here
    prod = 1
    has_odd = False
    for c in str(abs(n)):          # 取绝对值，避免负数的 '-' 号干扰
        d = int(c)                 # 当前数位的数字
        if d % 2 == 1:             # 是奇数就乘进去
            prod *= d
            has_odd = True
    return prod if has_odd else 0  # 一个奇数都没有时返回 0
    # 返回一个整数  return an integer


print(sat(sol()))
