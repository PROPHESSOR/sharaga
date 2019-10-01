#!/usr/bin/python
# coding: utf-8

from datetime import date

def S(D, percent, iteration):
    return D * ((1 + (percent * 30 * iteration) / (iteration * 360)) ** iteration)

def V(D, percent, iteration):
    return D * (((1 + (percent * 30 * iteration) / (iteration * 360)) ** iteration) - 1)

deposit = float(raw_input("Введите сумму депозита: >> "))
period  = int(raw_input("Введите строк (мес.): >> "))
percent = int(raw_input("Введите процентную ставку (%): >> ")) / 100.0

iteration = 0

iterations = [] # [start[2], start[1], days, end[2], end[1], d]

while iteration < period: # TODO: for
    iteration += 1

    d = V(deposit, percent, iteration)

    print 'Месяц 1-%d: %f' % (iteration, round(d, 2))

    iterations.append(d)

print 'Таблица для клиента:'
client_sum = deposit

for (idx, it) in enumerate(iterations):
    print 'Месяц %d = %f' % (idx + 1, round(it if idx == 0 else it - iterations[idx - 1], 2))
    client_sum += it if idx == 0 else it - iterations[idx - 1]

client_sum = round(client_sum, 2)

print 'Сумма для клиента: %f' % client_sum

s = round(S(deposit, percent, period), 2)

print 'Проверка данных: %f == %f => %s' % (client_sum, s, 'Совпадают' if client_sum == s else 'Не совпадают')
