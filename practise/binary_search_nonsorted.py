def binary_search_sorted(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search_rotated(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

def binary_search_unsorted(arr, target):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    sorted_arr = [1, 3, 5, 7, 9]
    unsorted_arr = [9, 5, 1, 7, 3]

    target = 7

    index_sorted = binary_search_sorted(sorted_arr, target)
    index_unsorted = binary_search_unsorted(unsorted_arr, target)

    print(f"Index of {target} in sorted array: {index_sorted}")
    print(f"Index of {target} in unsorted array: {index_unsorted}")

if __name__ == "__main__":
    main()