import sys

# assumes left_arr and right_arr are sorted
def merge(left_arr, right_arr):
    i, j = 0, 0
    arr = []

    # compare leftmost elements of both arrays and 
    # append lower value to new array until we 
    # reach the end of either
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr.append(left_arr[i])
            i += 1
        else:
            arr.append(right_arr[j])
            j += 1

    # append the rest of the values if non-empty
    if i < len(left_arr):
        arr += left_arr[i:]
    
    # append the rest of the values if non-empty
    if j < len(right_arr):
        arr += right_arr[j:]

    return arr

# O(nlogn)
def mergesort(arr):
    if len(arr) == 1:
        return arr
    else: 
        m = len(arr) // 2
        return merge(mergesort(arr[:m]), mergesort(arr[m:]))


if __name__ == '__main__':
    arr = [int(x) for x in sys.argv[1:]]
    print(mergesort(arr))