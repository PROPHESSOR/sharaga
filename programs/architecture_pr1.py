#!/bin/python
# coding: utf-8

def removeBinPrefix(x):
    return bin(x).replace("0b", "")

class BinNumber():
    def __init__(self, strbinnumber):
        self.strbinnumber = strbinnumber
        self.binnumber = int(strbinnumber, 2)

    def binprint(self):
        print("Прямой код: %s" % self.strbinnumber)
        if self.binnumber < 0:
            tmp = ~self.binnumber
            print("Обратный код: %s" % removeBinPrefix(tmp))
            print("Дополнительный код: %s" % removeBinPrefix(tmp + 1))


a = BinNumber('101')

a.binprint()
