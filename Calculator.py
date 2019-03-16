def print_menu():
    print ''' Please Choose an option::
                    1. Add
                    2. Substract
                    3. Multiply
                    4. Divide
                    5. Exit
        '''
    option = input("Enter: ")
    return option

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def devide(a,b):
    return "Devisor can not be 0. Invalid operation" if b ==0 else a/b

def main():
    exit_code = 0
    while not exit_code:
        operation = print_menu()
        if operation == 5:
            break
        a = input('Enter first number : ')
        b = input('Enter second number: ')
        print "Result: ",
        if operation ==  1:
            print "%d" % add(a,b)
        elif operation == 2:
            print sub(a, b)
        elif operation == 3:
            print mult(a, b)
        elif operation == 4:
            print devide(a=a, b=b)
        else:
            print "Invalid chioce!!"
        print "Do you want to quit?  press Y to continue"
        if raw_input().upper() == 'Y':
          exit_code = 1
    print "Thank you!!"  

if __name__ == '__main__':
    main()