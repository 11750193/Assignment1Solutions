import math

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
    a, b, c = float(coeffs[0]), float(coeffs[1]), float(coeffs[2])

    if a == 0.0:                      # 退化成一元一次方程 b x + c = 0
        return -c / b if b != 0.0 else 0.0

    disc = b * b - 4.0 * a * c        # 判别式
    if disc < 0.0:                    # 无实根（本题只要求返回某个解，取重根的实部）
        disc = 0.0

    # 数值稳定的求根公式：先算 q = -(b + sign(b) * sqrt(disc)) / 2，两根为 q/a 和 c/q。
    # 若直接算 (-b + sqrt(disc)) / (2a)，当 b 与 sqrt(disc) 接近时会发生相近数相减而丢精度，
    # 误差可能超过 sat() 要求的 1e-6。
    q = -0.5 * (b + math.copysign(math.sqrt(disc), b))
    if q == 0.0:                      # b = 0 且 disc = 0，此时 0 就是根
        return 0.0

    # 两个根都是合理解，取绝对值较小的那个：根很大时 a*x^2 与 b*x 会大到把常数项 c 淹没，
    # sat() 在该根处无论如何都算不出小于 1e-6 的残差，只有小根才能被验证。
    x1, x2 = q / a, c / q
    return x1 if abs(x1) <= abs(x2) else x2
    # 返回一个浮点数    return a floating point number


print(sat(sol()))
