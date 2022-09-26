#!/usr/bin/env python3
import sys

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        self.total_time: int = selection_time + shipping_time

def sort(orders_to_sort):
    
    for i in range(len(orders_to_sort)):
        minimum = i
        for j in range(i + 1, len(orders_to_sort)):
            if orders_to_sort[j].total_time < orders_to_sort[minimum].total_time:
                swapElementsInList(orders_to_sort, minimum,j)
                minimum = j

    return orders_to_sort

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

    list_of_orders = sort(list_of_orders)


    for order in list_of_orders:
        print(order.id, end =' ', file=sys.stdout)
    print("\n", file=sys.stdout)



    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''