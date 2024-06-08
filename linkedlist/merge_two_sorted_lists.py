def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

def main():
    # Example usage
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merged_list = merge_two_sorted_lists(list1, list2)
    print(merged_list)

if __name__ == "__main__":
    main()