import queue

my_Q = queue.Queue()

my_Q.put(1)
my_Q.put(2)
my_Q.put(3)
elem = my_Q.get()
print(elem)