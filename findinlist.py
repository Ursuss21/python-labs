from random import randint
import time

def print_duration(start, end):
    print("time: %.12fs" % (end - start))

def linear_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return True
    return False

def in_operator(list, element):
    if element in list:
        return True
    return False

def count_function(list, element):
    if list.count(element):
        return True
    return False

long_list = [randint(0, 3000) for element in range(1000000)]

start_time = time.time()
print(linear_search(long_list, -1))
end_time = time.time()
print_duration(start_time, end_time)

start_time = time.time()
print(in_operator(long_list, -1))
end_time = time.time()
print_duration(start_time, end_time)

start_time = time.time()
print(count_function(long_list, -1))
end_time = time.time()
print_duration(start_time, end_time)
