class node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkList:

    def __init__(self):
        self.head=None

    def add_b(self):
        data=int(input("Enter the data at BIGINNING>>>"))
        newNode=node(data)
        n=self.head
        if self.head is None:
            self.head=newNode
        else:
            n.prev=newNode
            newNode.next=self.head
            self.head=newNode

    def display_F(self):
        #fix bug
        if self.head is None:
            print("the list is empty !!")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" | ")
                n=n.next

    def display_B(self):
        #fix bug
        if self.head is None:
            print("the list is empty !!")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(n.data,end=" | ")
                n=n.prev


    # def display_B(self):
    #     if self.head is None:
    #         print("the list is empty !!")
    #     else:
    #         n=self.head
    #         while n.next is not None:
    #             n=n.next
    #         while n is not None:
    #             print(n.data,end=" | ")
    #             n=n.prev

    def add_e(self):
        data=int(input("enter the data at the ENDING>>>"))
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            newNode.prev=n.data
            n.next=newNode

    def add_m(self):
        data=int(input("enter the data at the MIDDILE>>>"))
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            place= int(input("enter the place after which you want to add>>>"))
            n=self.head
            while True:
                if n.data==place:
                    newNode.next=n.next
                    n.next=newNode
                    n.next.prev=newNode
                    newNode.prev=n.data

                    return
                else:
                    n=n.next

    def delete_b(self):
        #fix bug
        if self.head is None:
            print("the list is empty !!")
        elif self.head.next is None:
            self.head=None
        else:
            n=self.head
            self.head=n.next
            n.next.prev=None


a=DoubleLinkList()
Break=True
while Break:
    print("<<<<<<LINKED LIST>>>>>>>\n""<<<<<SELECT OPTION>>>>>>\n"
          "1. ADDING AT BEGGINNING = 1  |"" 5. DELETING IN ENDING = 5      |"" 7. SEARCHING THE ELEMENT = 7            |\n"
          "2. ADDING AT ENDING = 2      |"" 4. DELETING IN BEGGINNING = 4  |"" 8. DISPLAY ALL ELEMENT FORWORD = 8      |\n"
          "3. ADDING IN THE MIDDLE = 3  |"" 6. DELETING IN THE MIDDLE = 6  |"" 9.DISPLAY BACKWORD = 9 |"" 10. EXIT = 10  |"
          )
    print()
    opt=int(input("ENTER THE OPTION>>> "))
    print()
    if opt==1:
        a.add_b()
    elif opt==2:
        a.add_e()
    elif opt==3:
        a.add_m()
    elif opt==4:
        a.delete_b()
    # elif opt==5:
    #     a.delet_e()
    # elif opt==6:
    #     a.delete_m()
    # elif opt==7:
    #     a.search()
    elif opt==8:
        a.display_F()
    elif opt==9:
        a.display_B()
    elif opt==10:
        Break=False
    else:
        print("enter the correct option (1-9)")


