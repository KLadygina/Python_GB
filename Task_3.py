""" Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4] """



numbers_1 = [1, 1, 2, 3, 4, 5, 5]
numbers_2 = []
for i in numbers_1:
    j = i + 1
    while j < len(numbers_1):
        # print(f'{numbers_1[i]}, {numbers_1[j]}')
        if(numbers_1[i] != numbers_1[j]):
            print(numbers_2.append(numbers_1[i]), end = " ")
        j += 1
