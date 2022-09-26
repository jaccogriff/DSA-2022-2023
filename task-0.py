from typing import List

def find_maximum(arr: List[int]):
    # TODO: Implement a program that finds the maximum value in an array and returns it.

    max_value = arr[0]

    for element in arr:
        if element > max_value:
            max_value = element
    
    return max_value

if __name__ == "__main__":
    # get input array
    arr_str: str = input()
    arr: List[int] = list(map(int, arr_str.split(' ')))

    # print maximum value of array
    print(find_maximum(arr))
