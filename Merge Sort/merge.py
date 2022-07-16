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

list1 = [1,2,7,8]
list2 = [3,4,5,6]

print(merge(list1, list2))

