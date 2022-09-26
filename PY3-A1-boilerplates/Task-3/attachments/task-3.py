#!/usr/bin/env python3
from cmath import pi
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

def sort(orders_to_sort, left, right):
    if left >= right: return
    j = partition(orders_to_sort, left, right)
    sort(orders_to_sort, left, j)
    sort(orders_to_sort, j + 1, right)

def partition(orders_to_sort, left, right):
    pivot = orders_to_sort[left]
    i = left + 1

    for j in range(left + 1,right):
        if orders_to_sort[j] < pivot:
            swapElementsInList(orders_to_sort, j, i)
            i += 1

    swapElementsInList(orders_to_sort, left, i - 1)
 
    return i - 1

    

def swapElementsInList(list, i, j):
    element_at_i = list[i]
    element_at_j = list[j]

    list[i] = element_at_j
    list[j] = element_at_i

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

    sort(list_of_orders, 0, len(list_of_orders))


    for order in list_of_orders:
        print(order.id, end =' ', file=sys.stdout)
    print("\n", file=sys.stdout)



    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with orders_to_sort new line.
            i.e: 1 2 3 4 5 6\n
    '''