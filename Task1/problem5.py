# 不要修改这个函数 sat()    do not modify this function
def sat(x: float, coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    return abs(a * x ** 2 + b * x + c) < 1e-6

def sol(coeffs=[2.5, 1.3, -0.5]):
    """
    Find any (real) solution to:  a x^2 + b x + c = 0 where coeffs = [a, b, c].
    For example, since x^2 - 3x + 2 has a root at 1, sat(x = 1., coeffs = [1., -3., 2.]) is True.
    求一元二次方程的任意一个解：a x^2 + b x + c = 0，其中a, b, c 为参数。
    如：1 是x^2 - 3x + 2 = 0 的一个根/解，函数sat(x = 1., coeffs = [1., -3., 2.])将返回True
    """
    # TODO: 从下一行开始写你的代码 your implementation here
    a,b,c= coeffs
    d=b*b-4*a*c
    e=d**0.5
    x=(-b-e)/(2*a)

    return x # 返回一个浮点数    return a floating point number


print(sat(sol()))
