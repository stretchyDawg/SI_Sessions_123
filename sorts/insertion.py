

def swap(a_list, index1, index2):
    temp = a_list[index1]
    a_list[index1] = a_list[index2]
    a_list[index2] = temp

def shift(a_list, index):
    while index > 0 and a_list[index-1] > a_list[index]:
        swap(a_list, index, index-1)
        index -= 1

def insertion_sort(a_list):
    for index in range(len(a_list)):
        shift(a_list, index)
        
        
        
        
        
        
        
def shift_wo_swap(a_list, index):
    hold = a_list[index]
    hold_index = index
    while hold_index > 0 and hold < a_list[hold_index-1]:
        a_list[hold_index] = a_list[hold_index-1]
        hold_index -= 1
    a_list[hold_index] = hold
    
def insertion_sort_wo_swap(a_list):
    for index in range(len(a_list)):
        shift_wo_swap(a_list, index)
        
def main():
    test = [2, 3, 1, 4, 7, 5, 7, 1, 2, 4, 243, 242, 2, 141, 34, 134, 12, 34, 66]
    print(test)
    swap(test, 2, 3)
    print(test)
    
    insertion_sort(test)
    print(test)
    
    test2 = [2, 3, 1, 4, 7, 5, 7, 1, 2, 4, 243, 242, 2, 141, 34, 134, 12, 34, 66]
    insertion_sort_wo_swap(test2)
    print(test2)
    
if __name__ == "__main__":
    main()