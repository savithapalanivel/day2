class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=none
class linkedlist:
    def __init__(self):
        self.head=none
        
    def __atbeginning(self,dataval):
        newnode=node(dataval)
        newnode.nxt=head
        head=newnode
list=linkedlist()
list.head=node("mon")
e2=node("tues")
e3=node("wed")
list.head.nxt=e2
e2.nxt=e3
list.atbeginning("ajay")
list.printlist()   
                


