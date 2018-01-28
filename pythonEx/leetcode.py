# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:48:56 2018

@author: PCTech
"""

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # accepted solution 1
        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        # a = pre.next
        # b = a.next
        # tmp = b.next
        # pre.next, b.next, a.next = b, a, tmp
        # pre = a
        # return self.next
        

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
        



        
