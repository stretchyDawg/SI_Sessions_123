

def split(a_list):
    mid = len(a_list)//2
    left = a_list[:mid]
    right = a_list[mid:]

    return left, right

def merge(left, right):
    merged = []
    left_index = 0
    left_len = len(left)
    right_index = 0
    right_len = len(right)
    
    while left_index < left_len and right_index < right_len:    # As long as you haven't reached the end of either list
        if left[left_index] <= right[right_index]:        
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    if left_index < left_len:
        merged += left[left_index:]
    else:
        merged += right[right_index:]
        
    return merged

def merge_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        left, right = split(a_list)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)

def main():
    test = [2, 3, 1, 4, 7, 5, 7, 1, 2, 4, 243, 242, 2, 141, 34, 134, 12, 34, 66]
    print(test)
    print(merge_sort(test), end = "\n\n")
    
    test2 = [2, 3, 1, 4, 7, 5, 7, 0, 0]
    print(test2)
    print(merge_sort(test2))

if __name__ == "__main__":
    main()