class Node:
    def __init__(self, x, prev):
        self.data = x
        self.next = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = Node
        self.size = 0

    def print_all_elements(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def insert(self, x):
        new_node = Node(x, None)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def erase(self, i):
        if i == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            prev = self.head
            cur = self.head.next
            j = 1
            while j < i:
                cur = cur.next
                prev = cur
            prev.next = cur.next
            if cur == self.tail:
                self.tail = prev
        self.size -= 1


class StackLinkedList:
    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        new_node = Node(item, self.list.head)
        self.list.head = new_node

    def pop(self):

        if self.list.head is None:
            return None

        elif self.list.head.next is None:
            last = self.list.head.data
            self.list.head = None
            return last

        else:
            head_item = self.list.head.data
            self.list.head = self.list.head.next
            return head_item

    def top(self):
        return self.list.head.data


class QueueLinkedList():
  def __init__(self):
    self.linkedlist = LinkedList()
  
  def push(self, item):
    self.linkedlist.insert(item)

  def pop(self): 
    if self.linkedlist.head is None:
            return None
    elif self.linkedlist.head.next is None:
        last = self.linkedlist.head.data
        self.linkedlist.head = None
        return last
    else:
        head_item = self.linkedlist.head.data
        self.linkedlist.head = self.linkedlist.head.next
        return head_item

  def front(self):
    if self.linkedlist.head is not None:
      return self.linkedlist.head.data
    return None
