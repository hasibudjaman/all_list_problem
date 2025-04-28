class BST:
    def __init__(self,key):
        self.key=key
        self.leftchild=None
        self.rightchil=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:

                self.leftchild=BST(data)
        else:
             if self.rightchil:
                 self.rightchil.insert(data)
             else:

                 self.rightchil=BST(data)

    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if data < self.key:
            if self.leftchild:
                self.leftchild.search(data)
            else:
                print("Node is not present in this tree")

        if data> self.key:
            if self.rightchil:
                self.rightchil.search(data)
            else:
                print("Node is not present in this tree")
                












root=BST(None)
root.insert(10)
list=[20,4,30,4,1,5,6]
for i in list:
    root.insert(i)
print()
root.search(4)


