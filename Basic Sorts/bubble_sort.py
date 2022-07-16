def bubble_sort(my_list): 
    for i in range(len(my_list) - 1, 0, -1): # iterates passes (decrementing val)
        for j in range(i): # makes the swaps
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j] # straight swap no temp
    return my_list

# decreasing number of swaps because after each pass, one item in the list has already been 
# sorted

my_list = [4,2,6,5,1,3]

print(bubble_sort(my_list))

# Working code: might be more inefficient though
# def sort(my_list):
#     for i in range(len(my_list)):
#         for j in range(i): # j will always be lesser than or equal to i
#             temp1 = my_list[i]
#             temp2 = my_list[j]
#             if temp2 > temp1:
#                 my_list[j] = temp1
#                 my_list[i] = temp2