from data_struct import ListNode, listHelper


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        reslist, head = None, None
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            res = x + y + carry
            carry = res // 10
            if reslist is None:
                reslist = ListNode(res % 10)
                head = reslist
            else:
                reslist.next = ListNode(res % 10)
                reslist = reslist.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            reslist.next = ListNode(carry)
        return head


if __name__ == '__main__':
    helper = listHelper()
    s = Solution()
    l1 = helper.build([9, 9])
    l2 = helper.build([1])
    res = s.addTwoNumbers(l1, l2)
    print(helper.to_list(res))