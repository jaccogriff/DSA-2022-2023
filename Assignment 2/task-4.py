# DSA Student 139
import sys
class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = ('1.1.1977', sys.maxsize)
        self.FRONT = 1
        self.last = 1 # index of first element with 0

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        if pos >= 2: 
            return int(pos / 2) 
        else: 
            return self.FRONT

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        child_pos = 2 * pos
        if child_pos <= self.maxsize: return child_pos 

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        child_pos = (2 * pos) + 1
        if child_pos <= self.maxsize: return child_pos 


    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return self.Heap[self.leftChild(pos)] == 0 and self.Heap[self.rightChild(pos)] == 0

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):

        first_value, second_value = self.Heap[fpos], self.Heap[spos]
        self.Heap[fpos], self.Heap[spos] = second_value, first_value

    # Function to insert a node into the heap
    def insert(self, element):
        self.Heap[self.last] = element

        new_value_inx = self.last
        parent_inx = self.parent(self.last)
        
        while self.Heap[new_value_inx][1] > self.Heap[parent_inx][1]:
            self.swap(parent_inx, new_value_inx)
            new_value_inx = parent_inx
            parent_inx = self.parent(new_value_inx)

        self.last += 1


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
        return self.Heap[self.FRONT]


# Driver Code
if __name__ == "__main__":
    input = input()
    input = input.split(";")
    dates = []
    values = []
    for d in input:
        date = d.strip().split(',', 2)
        dates.append(date[0])
        values.append(date[2])

    values = [int(x) for x in values]
    tuples = list(zip(dates, values))
    heap = MaxHeap(len(tuples) + 1)
    for t in tuples:
        heap.insert(t)

    max_reading = heap.extractMax()

    print(f'{max_reading[0]},{max_reading[1]}')

