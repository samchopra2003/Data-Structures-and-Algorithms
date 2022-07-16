def selection_sort(my_list):
    for i in range(len(my_list) - 1): # up to penultimate item because no need to compare last item with last item (efficiency)
        min_index = i
        for j in range(i + 1, len(my_list)): # important!- since min item has been placed correctly after each pass, no need to run it as many times as first time
            if my_list[j] < my_list[min_index]: 
                min_index = j   # Change min index if ahead item is lower
        my_list[min_index], my_list[i] = my_list[i], my_list[min_index] # swap vals to make sure min index num is positioned correctly
    
    return my_list

my_list = [4,2,6,5,1,3]

print(selection_sort(my_list))
        