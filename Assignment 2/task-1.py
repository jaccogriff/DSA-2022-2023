# DSA Student 139

from array import array


def find_max_ind(arr):
    """

    :param arr: Array of integers
    :return: Index of the maximum
    """
    max_idx = 0

    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    
    return max_idx


if __name__ == "__main__":
    # get input array
    str_array = input()
    arr_str = str_array.rstrip()
    arr = list(map(int, arr_str.split(' ')))

    # print maximum value of array
    print(find_max_ind(arr))
