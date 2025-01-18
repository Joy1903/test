# Просто так охоота linked list реализовать 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val=None):
        self.head = val
        self.size = 0

    def addAtHead(self, val):
        newNode = Node(val, self.head)
        self.head = newNode
        self.size += 1
    
    def addAtIndex(self, val, index):
        currentNode = self.head
        if index >= self.size or index < 0:
            return False
        for i in range(0, index-1):
            currentNode = currentNode.next
        oldNode = currentNode
        newNode = Node(val, currentNode.next)
        oldNode.next = newNode
        self.size +=1

    def printList(self):
        curruntNode = self.head
        while curruntNode:
            print(curruntNode.val)
            curruntNode = curruntNode.next
        
myList = LinkedList()
myList.addAtHead(4)
myList.addAtHead(3)
myList.addAtHead(2)
myList.addAtHead(1)
myList.printList()
print("\n")
myList.addAtIndex(0, 3)
myList.printList()
        