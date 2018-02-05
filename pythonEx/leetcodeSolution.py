from listNode import ListNode

class Solution:
    def __init__(self, attr1, attr2, attrDefalt = ''):
        self.m_attr1 = attr1
        self.m_attr2 = attr2
        
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    # def swapPairs(self, head):
    #     # """
    #     # :type head: ListNode
    #     # :rtype: ListNode
    #     # """

    #     # accepted solution 1
    #     pre, pre.next = self, head
    #     while pre.next and pre.next.next:
    #         a = pre.next
    #         b = a.next
    #         tmp = b.next
    #         pre.next, b.next, a.next = b, a, tmp
    #         pre = a
    #     return self.next
        

        # accepted solution 2
        # res = head
        
        # if head:
        #     if head.next:
        #         newHead = self.swapPairs(head.next.next)
        #         tmp = head.next
        #         tmp.next = head
        #         head.next = newHead
        #         res = tmp
            
        # return res
        
    def isIsomorphic(self, s, t):
        # """
        # :type s: str
        # :type t: str
        # :rtype: bool
        # """
        
         # accepted solution 1
        found = {}
    
        for i in range(len(s)):
            if s[i] in found:
                if not found[s[i]] == t[i]:
                    return False

            else:
                if t[i] in found.values():
                    return False
                found[s[i]] = t[i]

        return True

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        print(" ==================================================== ")
        print("nums = ", nums)
        print("target = ", target)
        print("index = ", index)
        print("path = ", path)
        print("res = ", res)
        if target < 0:
            print("back tracing")
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

    def removeNthFromEnd(self, head, n):
        # """
        # :type head: ListNode
        # :type n: int
        # :rtype: ListNode
        # """

    def myDbg(self):
        print("I love python")