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












root=BST(None)
root.insert(10)
list=[20,4,30,4,1,5,6]
for i in list:
    root.insert(i)
    


