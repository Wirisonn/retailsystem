trolley_1 = [1, 2, 3, 4, 6,]

def enqueue(x):
    trolley_1.append(x)
    print(trolley_1)

def dequeue():
    trolley_1.pop()
    print(trolley_1)

enqueue(3)
enqueue(4)
enqueue(4)
enqueue(4)
enqueue(4)
enqueue(10)
dequeue()

#for i in range(len(trolley_1)):
#    print(trolley_1[i])

set_trolley = set(trolley_1)
print(set_trolley)

final_trolley = list(set_trolley)
print(final_trolley)

for i in range(len(final_trolley)):
    def count_items(lst, x):
        quantity  = lst.count(x)
        return quantity
    lst = trolley_1
    x= final_trolley[i]
    print('{} to {}'.format(x, count_items(lst, x)))


