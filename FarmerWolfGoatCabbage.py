my_list = [[0, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 1, 1],
           [0, 1, 0, 0],
           [0, 1, 0, 1],
           [0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 1],
           [1, 0, 1, 0],
           [1, 0, 1, 1],
           [1, 1, 0, 0],
           [1, 1, 0, 1],
           [1, 1, 1, 0],
           [1, 1, 1, 1]]

to_remove = []  # Create a list to store indices of elements to remove

for i in range(len(my_list)):
    if (my_list[i][2] == my_list[i][3]) and (my_list[i][2] != my_list[i][0]):
        to_remove.append(i)
    if (my_list[i][1] == my_list[i][2]) and (my_list[i][2] != my_list[i][0]):
        to_remove.append(i)

# Remove elements from the original list using indices stored in to_remove list
for index in sorted(to_remove, reverse=True):
    my_list.pop(index)

print(my_list)