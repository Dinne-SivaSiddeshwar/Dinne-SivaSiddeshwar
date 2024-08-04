class Node:
  def __init__(self,data=Node):
    self.data = data
    self.data = None
class sll:
  def __init__(self):
    self.head = None
# print the linked list
  def listprint(self):
    printval = self.head
    print("Linked list")
    while printval is not None:
      print(printval.data)
      printval = printval.next
  def AddBeg(self, newdata):
    NewNode = Node(newdata)
    # update the new nodes val to existing node
    NewNode.next = self.head
    self.head = NewNode
l = sll()
l.head = Node("mon")
e2 = Node("tue")
e3 = Node("wed")

l.head.next = e2
e2.next = e3

l.AddBeg("sun")
l.listprint()
