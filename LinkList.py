'''
Link List in python
'''
class Node(object):
    """
    Node class
    """
    def __init__(self):
        # define the fields 
        data = None
        right = None
    def set_data(self,data):
        self.data = data
    def get_next(self):
        return self.right 
    def set_next(self,node):
        self.right =  node
    

class LinkList(object):
    
    def __init__(self):
        '''
        Return head
        '''
        head = Node()
        return head
    def insert(self,data,pos=None):
        if pos is None:
            '''
            Insert at end
            '''
            temp = self.head
            while temp.get_next() != None:
                temp = temp.get_next()
            t = Node()
            t.set_data(data)
            temp.set_next(t)
        else:
            if pos.upper() == "START":
                temp = Node()
                temp.set_data(data)
                temp.set_next(self.head.get_next())
                self.head.set_next(temp)
        
def main():
    

if __name__ == '__main__':
    main()
    print("Hello")