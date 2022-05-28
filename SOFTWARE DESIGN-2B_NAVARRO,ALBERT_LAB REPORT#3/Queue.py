#Queue(FIFO)

queue=[]
def enqueue():
    ele = input('Enter the element: ')
    queue.append(ele)
    print(ele, 'is added to queue')

def dequeue():
    if not queue:
        print('queue is empty!')
    else:
        ele = queue.pop(0)
        print('removed element: ', ele)

def display():
    print(queue)

print('Choose the operation\n1.ADD\n2.REMOVE\n3.SHOW\n4.QUIT')
while True:
    opt = int(input('Enter the operation: '))
    if opt == 1:
        enqueue()
    elif opt == 2:
        dequeue()
    elif opt == 3:
        display()
    elif opt == 4:
        break
    else:
        print('Error: Invalid Option')

