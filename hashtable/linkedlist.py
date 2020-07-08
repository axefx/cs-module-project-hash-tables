class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def insert(self,value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def append(self, value):
        pass

    def delete(self,value):
        cur = self.head
        if cur.value == value:
            self.head = self.head.next
            return cur

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(11)
    ll.insert(22)
    print(ll)