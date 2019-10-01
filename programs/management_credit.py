#!/usr/bin/python
# coding: utf-8

PBB = 400000
PERCENT = 0.3
PERIOD = 5

def PV(iteration):
    return round((1 / (1 + PERCENT / 12) ** iteration), 4)

PVs = 0

for i in range(PERIOD):
    tmp = PV(i + 1)
    PVs += tmp
    print 'PV(%d): %f' % (i + 1, tmp)

print 'PVs: %f' % PVs

A = round(PBB / PVs, 2)# 86102.97

def calc(pbb):
    percent = round((pbb * PERCENT * 30) / 360, 2)
    body = A - percent
    kbb = round(pbb - body, 2)
    print 'PBB: %f, Body: %f, Percent: %f, Ann: %f, Kbb: %f' % (pbb, body, percent, A, kbb)
    return kbb

pbb = PBB

for i in range(PERIOD):
    print i + 1,
    pbb = calc(pbb)

