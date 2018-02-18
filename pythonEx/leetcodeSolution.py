# from listNode import ListNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, attr1, attr2, attrDefalt = ''):
        self.m_attr1 = attr1
        self.m_attr2 = attr2

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        for i in range (len(nums)):
            # print("i = ",i,"j = ",j)
            if j>=len(nums):
                # print("first break")
                break

            if nums[j] == nums[i]:
                while nums[j] == nums[i]:
                    j += 1
                    # print("j = ",j)
                
                    if j>=len(nums):
                        # print("second break")
                        break

                # print("assign to num[i+1]")
                nums[i+1] = nums[j]

            j += 1

        # print("last i = ",i)
        # print(nums)
        # print("finally")

        res = []
        for index in range (0,i+1):
            # print("index = ",index)
            res.append(nums[index])
        print(res)
        return res
        
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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = l1
        last = l1
        linked = 0
        while l1 or l2:
            if l1:
                sum1 = l1.val
            else:
                sum1 = 0
            if l2:
                sum2 = l2.val
            else:
                sum2 = 0
            sum = sum1 + sum2 + carry
            carry = 0
            if sum>=10:
                carry = 1
            res = sum % 10
            if l1:
                l1.val = res
                last = l1
                l1 = l1.next
                if l2:
                    l2 = l2.next
            else:
                l2.val = res
                if not linked:
                    last.next = l2
                    linked = 1
                last = l2
                l2 = l2.next
                
        if carry > 0:
            newNode = ListNode(carry)
            last.next = newNode
        return head

    # def removeNthFromEnd(self, head, n):
        # """
        # :type head: ListNode
        # :type n: int
        # :rtype: ListNode
        # """
        if not head:
            return None
        if not head.next:
            return None
        slow = head
        fast = head
        for i in range (n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            #last = slow
            slow = slow.next
        slow.next = slow.next.next
        
        return head


    def myDbg(self):
        print("I love python")
        pattern ="zhangyixin"
        print(pattern[3:])
        print(pattern[3])