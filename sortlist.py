list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

def sort_method(list_element):
    return (list_element[1], list_element[2])

list_to_sort.sort(key=sort_method, reverse=False)
list_to_sort_2.sort(key=sort_method, reverse=False)

print(list_to_sort)
print(list_to_sort_2)