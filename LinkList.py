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
        left = None
        right = None
    def set_data(self,data):
        self.data = data
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
