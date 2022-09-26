#!/usr/bin/env python3
import sys
import math


class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        self.total_time: int = selection_time + shipping_time

    def __le__(self, other):
        return self.total_time <= other.total_time
   
    def __lt__(self, other):
        return self.total_time < other.total_time

def sort(orders_to_sort):
    
    if (len(orders_to_sort) <= 1): return orders_to_sort

    halves = splitArray(orders_to_sort)

    return mergeSortedArrays( sort(halves[0]), sort(halves[1]) )

def splitArray(array_to_split):
    lengthOfA = math.floor(len(array_to_split)/2)

    arrayA, arrayB = [],[]
    for i in range(lengthOfA):
      arrayA.append( array_to_split[i] )
    
    for i in range(lengthOfA, len(array_to_split)):
      arrayB.append( array_to_split[i] )
    
    return (arrayA, arrayB)

def mergeSortedArrays(array_a , array_b ):
    j, i = 0, 0
    mergedArray = []
    jHasReachedEnd, iHasReachedEnd = False, False

    for k in range(len(array_a) + len(array_b)):
        if ( (array_a[i] <= array_b[j] or jHasReachedEnd) and not iHasReachedEnd ):
            mergedArray.append(array_a[i])
            if (i < len(array_a) - 1):
                i += 1
            else:
                iHasReachedEnd = True
        elif ( (array_b[j] < array_a[i] or iHasReachedEnd) and not jHasReachedEnd ):
            mergedArray.append(array_b[j])
            if (j < len(array_b) - 1):
                j += 1
            else:
                jHasReachedEnd = True

    return mergedArray


if __name__ == '__main__':
    '''
    Retrieves and splits the input
    '''
    data = input()
    data = data.split('; ')
    list_of_orders = []

    for d in data:
        id, selection_t, shipping_t = d.split(', ', 2)
        order: Order = Order(int(id), int(selection_t), int(shipping_t))
        list_of_orders.append(order)

    list_of_orders = sort(list_of_orders)


    for order in list_of_orders:
        print(order.id, end =' ', file=sys.stdout)
    print("\n", file=sys.stdout)



    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with orders_to_sort new line.
            i.e: 1 2 3 4 5 6\n
    '''