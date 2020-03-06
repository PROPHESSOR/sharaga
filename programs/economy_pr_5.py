#!/usr/bin/python3
# coding: utf-8

def nal(num):
    pdfo = round(num * 0.18, 2)
    print("ПДФО (18%) =", pdfo)
    mil = round(num * 0.015, 2)
    print("Военный сбор (1.5%) =", mil)
    out = round(num - pdfo - mil, 2)
    print("На руки =", num, "-", pdfo, "-", mil, "=", out)

print("Функции: nal(num) - рассчитать ПДФО и Военный сбор")
