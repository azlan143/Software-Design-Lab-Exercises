#Python Implementation of Stack using list

stack = []

#add items
def push():
    ele = input("Enter the element: ")
    stack.append(ele)
    print("Stack: ", stack)

#remove an element
def pop():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element: ", e)
        print("Stack: ", stack)

while True:
    print("Python Stack Implementation using List")
    print("1.push\n2.pop""\n3.quit")
    op = int(input("Select an operation: "))
    if op == 1:
        push()
    elif op == 2:
        pop()
    elif op == 3:
        break
    else:
        print("Invalid Opeartion!!!")
