# from listNode import ListNode

# Definition for singly-linked list.
class Solution:
    def __init__(self, attr1, attr2, attrDefalt = ''):
        self.m_attr1 = attr1
        self.m_attr2 = attr2

"""
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        A = []
        len_s = len(s)
        for i in range(len_s):
            ch = s[i]
            if ch in ['(','{','[']:
                A.append(ch)
            else:
                if len(A)<1:
                    return False
                    
                if ch == ')':
                    if A[-1] is '(':
                        A.pop()
                    else: 
                        return False
                if ch == ']':
                    if A[-1] is '[':
                        A.pop()
                    else: 
                        return False
                if ch == '}':
                    if A[-1] is '{':
                        A.pop()
                    else: 
                        return False
        
        if len(A)>0:
            return False
        
        return True
