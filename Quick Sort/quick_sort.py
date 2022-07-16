def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1): # loops goes upto end_index (end_index + 1 not included)
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort(my_list, left, right):
    if left < right:   # Base case: if left is equal to or greater than right
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index-1)  # quick sort to the left of pivot index
        quick_sort(my_list, pivot_index+1, right)  # quick sort to the right of pivot index
    return my_list

my_list = [4,6,1,7,3,2,5]

print(quick_sort(my_list, 0, 6))