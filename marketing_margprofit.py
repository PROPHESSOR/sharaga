# coding: utf-8

PRICE_BUY   = 3000  # Цена покупки
PRICE_SELL  = 10000 # Цена продажи
CONST       = 21000 # Постоянные траты
PROFIT      = 5000  # Желаемый доход

def marginalProfit(price, var, const):
    ''' price - выручка (цена); var - переменные траты; const - постоянные траты '''

    print 'Рассчёт маржинального дохода при цене', price, 'пер. тратам', var, 'пост. тратам', const
    md = price - var
    print 'МД =', md
    x = int(round(float(const) / float(md)))
    print 'x =', x, 'шт.'
    return (x, md)

def getPoint(price, var, const):
    ''' price - цена продажи; var - переменные траты; const - постоянные траты '''

    x = marginalProfit(price, var, const)[0]
    out = price * x
    print 'Точка безубыточности =', out
    return out

def zapasBezopasnosti(price, var, const): # FIXME:
    print '=== Рассчитываем запас безопасности ==='
    point = getPoint(price, var, const)
    zbez = price - point
    print 'Запас безопасности =', zbez
    k = float(zbez) / float(price)
    print 'Коэф. з.б. =', k

# zapasBezopasnosti(10000, 3000, 21000)


def buildTable(price, var, const, Profit, count=None):
    if count == None:
        count = marginalProfit(price, var, const + Profit)[0] # Количество, чтобы выйти в 0

    print 'Строим таблицу продажи', count, 'шт. по цене', price, 'потратив', const, 'в общем +', var, 'на штуту'
    # x = marginalProfit(price, var, const + Profit)[0]
    xprice = price * count
    print 'Выручка', xprice
    Var = count * var
    print 'Пер. траты', Var
    md = xprice - Var
    print 'Марж. дох.', md
    print 'Пост. траты', const
    profit = md - const
    print 'Прибыль', profit
    duty = profit * 0.18
    print 'Налог', duty
    cp = profit - duty
    print 'Чист. приб.', cp

# marginalProfit(PRICE_SELL, PRICE_BUY, CONST)
# marginalProfit(PRICE_SELL, PRICE_BUY, CONST + PROFIT)

# buildTable(PRICE_SELL, PRICE_BUY, CONST, PROFIT)
# buildTable(PRICE_SELL, PRICE_BUY, CONST, PROFIT, 8) # 8 x 3000
# buildTable(PRICE_SELL - PRICE_SELL * 0.12, PRICE_BUY, CONST, PROFIT, 8 + 8 * 0.16) # 8 x 3000


# buildTable(1300, 460 + 20, (54000-4000)/5 + 4000*52 + 4000*12 + 40000*12 + 5000*12, 25000, 160*52)
