# Helper function
def merge(list1, list2):    # we are working with two different sorted lists
    combined = []
    i = 0   # iterates through list1
    j = 0   # iterates through list2
    while i < len(list1) and j < len(list2): # once one list is empty loop will break
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:   # even if both vals are equal
            combined.append(list2[j])
            j += 1

    while i < len(list1):  # runs if list1 is not empty
        combined.append(list1[i])
        i += 1

    while j < len(list2):  # runs if list2 is not empty
        combined.append(list2[j])
        j += 1

    return combined

def merge_sort(my_list): # merge sort function
    if len(my_list) == 1:  # base case
        return my_list  # provides argument for left merge sort and right merge sort
    mid = int(len(my_list)/2)   # same thing as math.floor
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))   # recursion 
# once the list is broken down to 1 element, merge function kicks in to sort two lists
# one by one, and then we get a completely sorted list thanks to recursion!!!

my_list = [3,1,4,2]

print(merge_sort(my_list))
