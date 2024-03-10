class node:

    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:

    def __init__(self):
        self.head=None

    def add_b(self):
        data=int(input("enter the data at STARTING>>"))
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def add_e(self):
        data=int(input("enter the data at ENDING>>"))
        newNode=node(data)
        n=self.head
        if self.head is None:
            self.head=newNode
        else:
            while n.next is not None:
                n=n.next
            n.next=newNode

    def display(self):
        n=self.head
        if self.head is None:
            print("the list empty !!")
        else:
            while n is not None:
                print(n.data,end=" | ")
                n=n.next
            print()

    def add_m(self):
        data=int(input("enter the data at MIDDLE>>"))
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            place=int(input("After what number you want to add ? >>"))
            while True:
                if place==n.data:
                    newNode.next=n.next
                    n.next=newNode
                    return
                else:
                    n=n.next

    def delet_b(self):
        if self.head is None:
            print("the list is already empty !!")
        else:
            n=self.head
            self.head=n.next

    def delet_e(self):
        if self.head is None:
            print("the list is empty !!")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def delete_m(self):
        if self.head is None:
            print("the list is empty !!")
        else:
            data=int(input("enter the place after DELETION>>"))
            n=self.head
            while n.data!=data:
                n=n.next
            if n.next is None:
                print("there is no next element !! ")
            else:
                n.next=n.next.next


    def search(self):
        data=int(input("enter the element for searching>>>"))
        if self.head is None:
            print("the list is empty !!")
        else:
            n=self.head
            NotFound=True
            a=1
            while n is not None and n.data != data:
                n=n.next
                a+=1
            if n is not None:
                print("the element found at the place :",a)
                NotFound=False
            if NotFound:
                print("the element is not found !!")

    def Binary_search(self):
        if self.head is None:
            print("the list is already empty")
        else:
            data = int(input("enter the data for searching>>>"))
            n = self.head
            len=0
            while n is not None:
                len += 1
                n =n.next
            # print(len)
            low=0
            high=(len-1)
            b=0
            while low<=high:
                n2 = self.head
                mid=(low+(high+1))//2
                for i in range(mid):
                    n2=n2.next
                    b+=1
                if n2.data==data:
                    return b
                elif data<n2.data:
                    high=mid-1
                else: low=mid+1
        return -1

a=linklist()
Break=True
while Break:
    print("\n""<<<<<<LINKED LIST>>>>>>>\n""<<<<<SELECT OPTION>>>>>>\n"
          "1. ADDING AT BEGGINNING = 1\n"
          "2. ADDING AT ENDING = 2\n"
          "3. ADDING IN THE MIDDLE = 3\n"
          "4. DELETING IN BEGGINNING = 4\n"
          "5. DELETING IN ENDING = 5\n"
          "6. DELETING IN THE MIDDLE = 6\n"
          "7. SEARCHING THE ELEMENT = 7\n"
          "8. BINARY SEARCHING = 8\n"
          "9. DISPLAY ALL ELEMENT = 9\n"
          "10. EXIT = 10")
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
        a.delet_b()
    elif opt==5:
        a.delet_e()
    elif opt==6:
        a.delete_m()
    elif opt==7:
        a.search()
    elif opt==8:
        re=a.Binary_search()
        if re==-1:
            print("Not found !!!")
        else:
            print("Found !!!")
    elif opt==9:
        a.display()
    elif opt==10:
        Break=False
    # elif opt>10 or opt<0:
    #     print("enter only numbers between 1-10")
    else:
        print("enter the correct option (1-9)")