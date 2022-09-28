# DSA Student 139

def find_duplicate(arr, n):
    """

    :param arr: array with all sensory IDs
    :param n: length of the array
    :return: ID with duplicate measurement
    """
    ids_sum = 0
    for i in range(n):
        ids_sum += ids[i]

    return int (ids_sum - ((n - 1) * n/2))


if __name__ == "__main__":
    # get input array
    input = input()
    input = input.split(";")
    ids = []
    for d in input:
        id, value = d.rstrip().split(',', 1)
        ids.append(int(id))



    # compute the duplicate sensor
    n = len(ids)
    print(find_duplicate(ids, n))
