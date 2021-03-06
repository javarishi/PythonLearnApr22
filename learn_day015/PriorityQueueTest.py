from queue import PriorityQueue

customers = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list.
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((0, "Riya"))
customers.put((4, "Stacy"))
customers.put((10, "Niel"))

while not customers.empty():
    print(customers.get())
