class node:
    def __init__(self,d):
        self.data=d
        self.next=None

class Linkedlist_sort:

    def __init__(self):
        self.head=None
    def sorting(self):
        data=int(input("enter the data for sorting>>>"))
        newNode=node(data)
        n=self.head
        if self.head is None:
            self.head=newNode
        elif n.data>data:
            newNode.next=self.head
            self.head=newNode
        else:
            while n.next is not None and n.next.data < data:
                n = n.next
            newNode.next = n.next
            n.next = newNode

    def display(self):
        if self.head is None:
           print("still values not inserted !!!")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.next
            print()
a=Linkedlist_sort()
while True:
    a.sorting()
    a.display()