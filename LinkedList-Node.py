class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
        self.tail= self.head
        self.length =1

    def append(self,value):
        self.NewNode=Node(value=value)
        #self.NewNode.value = value
        self.tail.next = self.NewNode
        self.tail = self.NewNode
        self.length = self.length + 1

    def prepend(self,value):
        self.NewNode = Node(value=value)
        self.NewNode.next = self.head
        self.NewNode = self.head
        self.length = self.length + 1

    def printList(self):
        currentNode = self.head

        while currentNode!=None:
            print(currentNode.value)
            currentNode=currentNode.next

    def insert(self,index,value):
        leader = self.traversetoIndex(index-1)
        holdingPointer = leader.next
        self.NewNode = Node(value=value)
        leader.next = self.NewNode
        self.NewNode.next = holdingPointer
        self.length = self.length + 1

    def remove(self,index):
        currentNode = Node(value=0)
        leader = self.traversetoIndex(index=index)
        currentNode=leader.next
        leader.next = currentNode.next
        self.length = self.length - 1

    def traversetoIndex(self,index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter = counter + 1
        return currentNode



myLinkedList = LinkedList(10)
myLinkedList.append(15)
myLinkedList.append(10)
myLinkedList.printList()

