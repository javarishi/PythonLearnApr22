import queue

fifo = queue.Queue()
simple = queue.SimpleQueue() # Also FIFO
lifo = queue.LifoQueue() # Last in First Out
priority = queue.PriorityQueue() # Message Priority

# Adding / producing / send a message in queue - put method
message = "This is a Message for queue {} "
for eachID in range(1,11):
    fifo.put(message.format(eachID))
    lifo.put(message.format(eachID))
    simple.put(message.format(eachID))
    priority.put(message.format(eachID))

# Checking the Size
print("FIFO Size:: ", fifo.qsize())
print("LIFO Size:: ", lifo.qsize())
print("SIMPLE Size:: ", simple.qsize())
print("PRIORITY Size:: ", priority.qsize())

# getting the message from queue
fifo_get = fifo.get()
print("FIFO :: ", fifo_get)
lifo_get = lifo.get()
print("LIFO :: ", lifo_get)
simple_get = simple.get()
print("SIMPLE :: ", simple_get)
priority_get = priority.get()
print("PRIORITY :: ", priority_get)

print("FIFO Size:: ", fifo.qsize())
print("LIFO Size:: ", lifo.qsize())
print("SIMPLE Size:: ", simple.qsize())
print("PRIORITY Size:: ", priority.qsize())

