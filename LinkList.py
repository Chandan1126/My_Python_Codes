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
    

def main():
    

if __name__ == '__main__':
    main()