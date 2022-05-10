from threading import Thread
from random import randint

#Well, I started doing this code for a simple threading exercise(from University) 
#and I ended up liking the flexibility of the code in creating the threads.
#So now I'll put it on GitHub too :p

size = 1000000 #List size and maximum value of random int range.
thread_qt = 4 #You can change it from what you want, highest value tested: 8192.
exact_div = True #Some protection.

l = [randint(0,size) for i in range(size)]

#just testing :p
#l.sort()

if size % thread_qt == 0 and exact_div is True:
    ll = []

    for i in range(thread_qt):
        ll.append(l[i*(size//thread_qt):(i+1)*(size//thread_qt)])

    acc = [0]*thread_qt
    x = [None]*(thread_qt-1)

    def multithreaded_max(index):
        for i in range(size//thread_qt):
            if ll[index][i] > acc[index]:
                acc[index] = ll[index][i]

    for i in range(len(x)):
        x[i] = Thread(target=multithreaded_max, args=(i+1,)) #Starting from index=1, because we'll use index=0 with main thread :P
        x[i].start()

    #Reused code, we don't need to take a new code segment to process just the first list piece, since we have this method...
    multithreaded_max(0)

    for i in range(len(x)):
        x[i].join()

    print(f"Highest values ​​of each chunk of the list")
    for i in range(len(acc)):
        print(f"Thread {i+1}: {acc[i]}")
else:
    print(
    """
    The quotient between the size of the list
    and the number of slices to be processed in parallel
    is fractional, which will cause inequality in the 
    division of items between threads. To ignore this warning,
    open the script and change "exact_div" from True to False.
    """)