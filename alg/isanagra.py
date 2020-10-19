"""
判断t是否是s的异构词（字母个数相同，顺序不同）
解1：排序
解2：哈希表，

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_dict = {}
        if len(s)!=len(t):
            return False
        else:
            for value1, value2 in zip(t, s):
                t_dict[value1] += 1
                t_dict[value2] -= 1
        for item in t_dict.values():
          if item != 0:
            return False

        return True