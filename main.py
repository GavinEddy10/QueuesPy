from Node import *
n1 = Node(400)
n2 = Node(300)

q = Queue(n1, n2)
q.poll()
q.print_queue()