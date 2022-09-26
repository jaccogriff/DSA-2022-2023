import sys
class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = ('1.1.1977', sys.maxsize)
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):

        raise NotImplementedError

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):

        raise NotImplementedError

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):

        raise NotImplementedError

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):

        raise NotImplementedError

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):

        raise NotImplementedError

    # Function to heapify the node at pos
    def maxHeapify(self, pos):

        raise NotImplementedError

    # Function to insert a node into the heap
    def insert(self, element):

        raise NotImplementedError

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print(i)
            print("PARENT : " + str(self.Heap[i]) +
                  "LEFT CHILD : " + str(self.Heap[2 * i]) +
                  "RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):

        raise NotImplementedError


# Driver Code
if __name__ == "__main__":
    input = input()
    input = input.split(";")
    dates = []
    values = []
    for d in input:
        date = d.split(',', 2)
        dates.append(date[0])
        values.append(date[2])

    values = [int(x) for x in values]
    tuples = list(zip(dates, values))
    heap = MaxHeap(len(tuples) + 1)
    for t in tuples:
        heap.insert(t)

    heap.extractMax()

