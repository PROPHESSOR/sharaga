#!/usr/bin/env python3
#coding: utf-8

num = int(input("Введите количество подсетей: "))

if num < 2 or num >= 250 or not float(255 % num).is_integer():
    print("Неверное значение!")

computers = 255 // num

output = []

for i in range(0, 255 - computers + 1, computers + 1):
    output.append([i, i + 1, i + computers - 1, i + computers])
    #print(i, i + 1, i + computers - 1, i + computers)


def print_table(headers, values):
    v = [headers] + values

    for row in v:
        for col in row:
            # value
            print(col, end="")
            # separator
            print('\t|\t', end="")
        print()


def format_matrix(header, matrix, top_format, left_format, cell_format, row_delim, col_delim):
    table = [[''] + header] + [[name] + row for name, row in zip(header, matrix)]
    table_format = [['{:^{}}'] + len(header) * [top_format]] \
                 + len(matrix) * [[left_format] + len(header) * [cell_format]]
    col_widths = [max(
                      len(format.format(cell, 0))
                      for format, cell in zip(col_format, col))
                  for col_format, col in zip(zip(*table_format), zip(*table))]
    return row_delim.join(
               col_delim.join(
                   format.format(cell, width)
                   for format, cell, width in zip(row_format, row, col_widths))
               for row_format, row in zip(table_format, table))

#print(format_matrix(['Man Utd', 'Man City', 'T Hotspur', 'Really Long Column'], [[1, 2, 1, -1], [0, 1, 0, 5], [2, 4, 2, 2], [0, 1, 0, 6]], '{:^{}}', '{:<{}}', '{:>{}.3f}', '\n', ' | '))
'''print(format_matrix(
    ['Адрес сети', 'Начало', 'Конец', 'broadcast'],
    output,
    '{:^{}}', '>', '{:>{}}', '\n', ' | '
))
'''

print_table(['Адрес', 'Начало', 'Конец', 'broadcast'], output)
