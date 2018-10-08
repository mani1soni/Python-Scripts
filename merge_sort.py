'''

Merge sort is divided and conquer algorithm

'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)
    else:
        return arr


def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

ar = [4,5,2,1,3]
merge_sort(ar)