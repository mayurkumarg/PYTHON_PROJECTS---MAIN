def Binary_search(self):
    if self.head is None:
        print("the list is already empty")
    else:
        data = int(input("enter the data for searching>>>"))
        n = self.head
        len = 0
        while n is not None:
            len += 1
            n = n.next
        # print(len)
        low = 0
        high = (len - 1)
        b = 0
        while low <= high:
            n2 = self.head
            mid = (low + (high + 1)) // 2
            for i in range(mid):
                n2 = n2.next
                b += 1
            if n2.data == data:
                return b
            elif data < n2.data:
                high = mid - 1
            else:
                low = mid +1
            return-1