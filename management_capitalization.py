#!/usr/bin/python
# coding: utf-8

from datetime import date

def S(D, percent, days, iteration):
    return D * ((1 + (percent * days) / (iteration * 360)) ** iteration)

def V(D, percent, days, iteration):
    return D * (((1 + (percent * days) / (iteration * 360)) ** iteration) - 1)

deposit = 40000.0 # float(raw_input("Введите сумму депозита: >> "))
period  = 5 # int(raw_input("Введите строк (мес.): >> "))
percent = 0.18 # int(raw_input("Введите процентную ставку (%): >> ")) / 100.0
start   = '2019.02.14'.split('.') # raw_input("Введите дату взноса (гггг.мм.дд): >> ").split('.')

if len(start) != 3:
    print "Неверный формат даты"
    exit()

start = [int(start[0]), int(start[1]), int(start[2])]

start_date = date(start[0], start[1], start[2])

iteration = 0

iterations = [] # [start[2], start[1], days, end[2], end[1], d]

while iteration < period:
    iteration += 1

    end   = [start[0], start[1] + iteration,  start[2]]

    days  = (date(end[0], end[1], end[2]) - start_date).days

    d = V(deposit, percent, days, iteration)

    print '%d.%d - (%d дней) - %d.%d = %f' % (start[2], start[1], days, end[2], end[1], d)

    iterations.append([start[2], start[1], days, end[2], end[1], d])

print 'Таблица для клиента:'
client_sum = deposit

for (idx, it) in enumerate(iterations):
    print '%d.%d - (%d дней) - %d.%d = %f' % (it[0], it[1], it[2], it[3], it[4], round(it[5] if idx == 0 else it[5] - iterations[idx - 1][5], 2))
    client_sum += it[5] if idx == 0 else it[5] - iterations[idx - 1][5]

client_sum = round(client_sum, 2)

print 'Сумма для клиента: %f' % client_sum

s = round(S(deposit, percent, days, period), 2)

print 'Проверка данных: %f == %f => %s' % (client_sum, s, 'Совпадают' if client_sum == s else 'Не совпадают')
