from random import randint

names = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
letters = [name[0] for name in names]
print(letters)

list_length = 5
numbers = [[randint(1, 10) for x in range(4)] for element in range(list_length)]
print(numbers)