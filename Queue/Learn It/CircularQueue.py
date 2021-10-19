class CircularQueue:

    def __init__(self, a):
        self.a = a
        self.queue = [None] * a
        self.head = self.tail = -1

    # Add an element into the demo circular queue

    def enqueue(self, data_elements):

        if (self.tail + 1) % self.a == self.head:
            print('The demo circular queue does not have more space')

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data_elements
        else:
            self.tail = (self.tail + 1) % self.a
            self.queue[self.tail] = data_elements

    # Remove an element from the demo circular queue

    def dequeue(self):

        if self.head == -1:
            print('The demo circular queue is empty')

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.a
            return temp

    def printDemoCQueue(self):
        if self.head == -1:
            print('No element present in the demo circular queue')

        elif self.tail == self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= ' ')
        else:
            for i in range(self.head, self.a):
                print(self.queue[i], end= ' ')
                for i in range(0, self.tail + 1):
                    print(self.queue[i], end= ' ')
        print()


if __name__ == '__main__':
    obj = CircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print('Demo Queue after adding the elements')
    print(f'\nDemo : {obj.printDemoCQueue()}')

    obj.dequeue()
    print('Demo Queue after removing the elements')
    obj.printDemoCQueue()
