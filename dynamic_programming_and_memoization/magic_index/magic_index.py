# O(logn)
#
# Let the sorted array arr contain distinct integers
#
# If arr[i] > i for some index i, then arr[j] > j for all j > i.
# It follows that a magic index cannot exist for any index >= i.
# 
# On the other hand, assume that a magic index exists in arr.
# If arr[k] < k for some index k, then the magic index > k.
#
# These facts can be used to perform binary search to find the magic index.
def binary_search(arr):
    if type(arr) in [list, tuple]:
        if len(arr) > 1:
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == mid:
                    return mid
                elif arr[mid] > mid:
                    right = mid - 1
                elif arr[mid] < mid:
                    left = mid + 1

            return None
        else:
            return None
    else:
        raise TypeError('find expects a list or tuple')
        
# O(n)
def linear_search(arr):
    if type(arr) in [list, tuple]:
        if len(arr) > 1:
            for index, value in enumerate(arr):
                if index == value:
                    return index
            return None
        else:
            return None
    else:
        raise TypeError('find expects a list or tuple')

# O(1)
# If the sorted array arr contains distinct non-negative integers
def check_magic_index(arr):
    if type(arr) in [list, tuple]:
        if len(arr) > 1:
            return 0 if arr[0] == 0 else None
        else:
            return None
    else:
        raise TypeError('find expects a list or tuple')