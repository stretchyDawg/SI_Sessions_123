def partition(a_list, pivot):
    less = []
    same = []
    more = []
    
    for element in a_list:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            more.append(element)
        else:
            same.append(element)
            
    return less, same, more
    
def quicksort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less, same, more = partition(a_list, pivot)
        less_sorted = quicksort(less)
        more_sorted = quicksort(more)
        
        sorted_list = less_sorted + same + more_sorted
        return sorted_list

def main():
    test = [2, 3, 1, 4, 7, 5, 7, 1, 2, 4, 243, 242, 2, 141, 34, 134, 12, 34, 66]
    print(test)
    print(quicksort(test))

if __name__ == "__main__":
    main()