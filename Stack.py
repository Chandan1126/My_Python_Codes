#!/usr/bin/python
"""
Stack immplementation 
"""
class MyStack:
    
    def __init__(self, length=10):
        self.mystack = list()
        self.stack_lenght = length
    def push(self, data):
        if len(self.mystack) < self.stack_lenght:
            self.mystack.append(data)
        else:
            print "Not ample space to insert data. Stack Overflow!!"
    def pop(self):
        if len(self.mystack) <= 0:
            print "stack is empty. Stack underflow!!"
        else:
            return self.mystack.pop()
    def display(self):
        print "%s <- top" % self.mystack

if __name__ == "__main__":
    my_stack = MyStack()
    flag =  True
    while flag:
        print "\tChoose an option:\n\t1.Push\n\t2.Pop\n\t3.Display\n\t4.Exit"
        option = int(input("Enter an option: "))
        if option == 1:
            data = int(input("Enter data : "))
            my_stack.push(data=data)
        elif option == 2:
            print "Poped item is %d" % my_stack.pop()
        elif option == 3:
            my_stack.display()
        elif option == 4:
            print "Thank you!!"
            flag = False
        else:
            print "Please try again."
        if not flag:
            break
