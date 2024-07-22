class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class LinkedList:
        
        
    def append(self,data,track):
        new_node=Node(data)
        if track==None:
            track=new_node
            
        else:
            current=track
            while current.next!=None:
                current=current.next
            current.next=new_node 
        return track 
        
    def display(self,track):
        current=track
        while current!=None:
            print(current.data,end="->")
            current=current.next
        
        print("None")
        
    def reverse(self,track):
        prev=None
        curr=track
        while curr:
            next_temp=curr.next
            curr.next=prev
            prev=curr
            curr=next_temp
        return prev
        

link=LinkedList()
head=link.append(35,None)
head=link.append(45,head)
head=link.append(55,head)
head=link.append(65,head)
link.display(head)
head=link.reverse(head)
link.display(head)
