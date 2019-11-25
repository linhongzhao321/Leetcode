# coding=utf-8
"""
leetcode 70. climbing-stairs
url: https://leetcode-cn.com/problems/climbing-stairs/
"""


# def climbStairs(n):
#     """
#     方法1
#     :type n: int
#     :rtype: int
#     """
#
#     last_one_count = 1
#     last_two_count = 0
#
#     if n > 1:
#         for i in range(1, n ):
#             ltc = last_two_count
#             last_two_count = last_one_count
#             last_one_count += ltc
#             print(str(i) + ': ' + str(last_one_count) + ', ' + str(last_two_count))
#
#     return last_one_count + last_two_count


def climbStairs(n):
    """
    方法2 - Fibonacci-Formula
    :type n: int
    :rtype: int
    """

    sqrt5 = 5 ** 0.5
    fib_n = (((1 + sqrt5) / 2) ** (n + 1)) - (((1 - sqrt5) / 2) ** (n + 1))
    return int(fib_n / sqrt5)


if __name__ == '__main__':
    print(climbStairs(7))
