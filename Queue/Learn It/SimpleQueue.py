class SimpleQueue:

    def __init__(self):
        self.queue = list()

    def add_demo_element(self, element):
        # Add the above method to insert the element

        if element not in self.queue:
            self.queue.insert(0, element)
            return True
        return False

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    Queue = SimpleQueue()
    Queue.add_demo_element('Monday')
    Queue.add_demo_element('Tuesday')
    Queue.add_demo_element('Wednesday')
    print(Queue.size())
