# coding=utf-8
"""
leetcode 5. longest palindromic substring
url: https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


def longestPalindrome(s):
    """
    方法1
    中心扩展法
    :type s:str
    :rtype: str
    """
    if s == '':
        return ''
    p_len_max = 1
    p_sub_max = s[0]
    s_len = len(s)
    # move center
    for i in range(s_len):
        flag = 0
        substring_len = min(i, s_len - i - 1)

        # traversed substring
        for j in range(1, substring_len + 1):
            if s[i + j] != s[i - j]:
                break
            flag = j
        p_len = 2 * flag + 1
        if p_len > p_len_max:
            p_len_max = p_len
            p_sub_max = s[i - flag: i + flag + 1]

        # traversed substring
        flag = 0
        substring_len = min(i, s_len - i)
        for j in range(1, substring_len + 1):
            if s[i + j - 1] != s[i - j]:
                break
            flag = j
        p_len = 2 * flag
        if p_len > p_len_max:
            p_len_max = p_len
            p_sub_max = s[i - flag: i + flag]

    return p_sub_max


# def longestPalindrome(s):
#     """
#     方法2
#     动态规划
#     :type s:str
#     :rtype: str
#     """
#     for ch in s:


if __name__ == '__main__':
    # print(longestPalindrome('ac'))
    # print(longestPalindrome(''))
    print(longestPalindrome('abcda'))
    # print(longestPalindrome('cbbd'))
    # print(longestPalindrome('babad'))
    # print(longestPalindrome('aaaa'))
