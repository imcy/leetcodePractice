class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class listHelper():
    def build(self, list_node):
        cur, head = None, None
        for i, node in enumerate(list_node):
            if cur is None:
                head = ListNode(node)
                cur = head
            else:
                cur.next = ListNode(node)
                cur = cur.next
        return head

    def to_list(self, head):
        link_list = []
        while head is not None:
            link_list.append(head.val)
            head = head.next
        return link_list

if __name__ == '__main__':
    helper = listHelper()
    l = [1, 2, 3, 4]
    link = helper.build(l)
    print(helper.to_list(link))