# coding=utf-8
"""
leetcode 30. substring with concatenation of all words
url: https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
"""
import copy

from collections import Counter


def findSubstring(s, words):
    """
    滑动窗口
    640 ms/12.3 MB
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words:
        return []

    word_cnt_map = Counter(words)
    s_len = len(s)
    word_len = len(words[0])
    words_cnt = len(words)
    s_len_min = word_len * words_cnt
    i_max = s_len - s_len_min
    if i_max < 0:
        return []

    sub_index_list = []
    i = 0
    t_word_cnt_map = Counter()
    j = i
    while i <= i_max:
        t_words_cnt = 0
        j_max = i + s_len_min
        while j < j_max:
            j_next = j + word_len
            t_word = s[j: j_next]
            t_word_cnt_map[t_word] += 1
            t_words_cnt += 1
            # 不符合要求
            if t_word_cnt_map[t_word] > word_cnt_map[t_word]:
                break
            else:
                j = j_next

        # finish
        if j >= j_max:
            sub_index_list.append(i)
            t_word_cnt_map = Counter()
            i += 1
            j = i
        else:
            t_word_cnt_map = Counter()
            i += 1
            j = i

    # print(sub_index_list)
    return sub_index_list


if __name__ == '__main__':
    findSubstring("barfoofoobarthefoobarman", ["bar", "foo"])
    # findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
    # findSubstring("barfoothefoobarman", ["bar", "foo"])
