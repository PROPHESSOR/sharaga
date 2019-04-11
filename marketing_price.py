#!/usr/bin/python
# coding: utf-8

def percent(x):
    return float(x) / 100.0

def xpercent(x, percent):
    percnt = float(percent) / 100.0
    return (float(x) * percnt) / (percnt + 1.0)

def KB2RC(KB, TBp, BPp, CMp, duty, OMPp, AZp, overprice, USD=27.06, PDVp=20):
    '''
    KB      - Контрактная стоимость
    TBp     - Процент транспортных затрат
    BPp     - Процент посредникам
    CMp     - Процент страховки
    duty    - Процент пошлины
    OMPp    - Процент работе пограничников
    AZp     - Процент акцизный сбор
    Прибыль - Процент желаемой прибыли
    [USD]   - Курс доллара
    [PDBp]  - Процент ПДВ
    '''
    print 'KB =', KB
    TB = KB * percent(TBp)
    print 'TB =', TB
    BP = (KB + TB) * percent(BPp) 
    print 'ВП =', BP
    CM = (KB + TB + BP) * percent(CMp)
    print 'СМ =', CM
    MB = KB + TB + BP + CM
    print 'МВ =', MB
    MB *= USD
    print 'МВ (грн) =', MB
    OMP = MB * percent(duty)
    print 'ОМП =', OMP
    BM = MB * percent(OMPp)
    print 'ВМ =', BM
    AZ = (MB + OMP + BM) * percent(AZp)
    print 'АЗ =', AZ
    PDV = (MB + OMP + BM + AZ) * percent(PDVp)
    print 'ПДВ =', PDV
    CP = MB + OMP + BM + AZ + PDV
    print 'ЦП =', CP
    RC = CP + (CP * percent(overprice))
    print 'РЦ =', RC
    return RC

def RC2KB(RC, TBp, BPp, CMp, duty, OMPp, AZp, overprice, USD=27.06, PDVp=20):
    '''
    RC      - Розничная цена
    TBp     - Процент транспортных затрат
    BPp     - Процент посредникам
    CMp     - Процент страховки
    duty    - Процент пошлины
    OMPp    - Процент работе пограничников
    AZp     - Процент акцизный сбор
    Прибыль - Процент желаемой прибыли
    [USD]   - Курс доллара
    [PDBp]  - Процент ПДВ
    '''
    print 'РЦ =', RC
    PROFIT = xpercent(RC, overprice)
    print 'Прибыль =', PROFIT
    CP = RC - PROFIT
    print 'ЦП =', CP
    PDV = xpercent(CP, PDVp)
    print 'ПДВ =', PDV
    AZ = xpercent(CP - PDV, AZp)
    print 'АЗ =', AZ
    BM = xpercent(CP - PDV - AZ, OMPp)
    print 'ВМ =', BM
    OMP = xpercent(CP - PDV - AZ, duty)
    print 'ОМП =', OMP
    MB = (CP - PDV - AZ - BM - OMP) / USD
    print 'МВ =', MB, '$'
    CM = xpercent(MB, CMp)
    print 'СМ =', CM
    TB = xpercent(MB - CM, TBp)
    print 'ТВ =', TB
    BP = xpercent(MB - CM - TB, BPp)
    print 'ВП =', BP
    KB = MB - CM - TB - BP
    print 'КВ =', KB
    return KB

def makeprice(price, overprice, AZp, PDVp):
    ''' формирует цену на собственный товар
    price - Себестоимость
    overprice - Желаемый процент прибыли
    AZp - Процент АЗ
    PDVp - Процент ПДВ
    '''

    print 'Себестоимость =', price
    print 'Желаемая прибыль = ', overprice, '%'
    GC = price * (1 + percent(overprice))
    print 'ГЦ =', GC
    pAZ = GC * (1 + percent(AZp))
    print 'ГЦ + АЗ =', pAZ
    pPDV = pAZ * (1 + percent(PDVp))
    print 'ГЦ + АЗ + ПДВ = ', pPDV

    return (pPDV, pAZ, GC)

def minify(price, pAZ, pPDV, PDVp):
    ''' максимально уменьшает цену своего товара за счёт ПДВ
    price - Себестоимость
    pAZ - ГЦ + АЗ
    pPDV - ГЦ + АЗ + ПДВ
    PDVp - Процент PDV
    '''
    PK = xpercent(price, PDVp)
    print 'ПК =', PK
    PZ = pAZ * percent(PDVp)
    print 'ПЗ =', PZ
    B = PZ - PK
    print 'Б =', B
    RC = pPDV - B
    print 'РЦ =', RC
    return RC

def getprofit(RC, shopoverprice, price, pAZ=15, pPDV=20):
    ''' рассчитывает процент дохода
    RC - финальная цена
    shopoverprice - Наценка торговой точки
    price - Себестоимость
    pAZ - Процент АЗ
    pPDV - Процет ПДВ
    '''
    NZ = xpercent(RC, shopoverprice)
    print 'Наценка =', NZ
    clearRC = RC - NZ
    print 'Без наценки =', clearRC
    PDV = xpercent(clearRC, pPDV)
    print 'ПДВ =', PDV
    AZ = xpercent(clearRC - PDV, 15)
    print 'АЗ =', AZ
    GZ = (clearRC - PDV - AZ)
    print 'ГЗ =', GZ
    RB = (GZ / price) * 100 - 100
    print 'Рентабельность =', RB, ('~ %d%%' % round(RB))

    return RB

if __name__ == "__main__":
    # calculate(912, 10, 5, 14, 0.2, 10, 15, 25)
    print 'Функции: KB2RC, RC2KB, makeprice, minify'
    # print help(KB2RC)
    # print help(RC2KB)
    RC = KB2RC(912, 10, 5, 14, 0.2, 10, 15, 25)
    print '==== Ищем обратно ===='
    KB = RC2KB(RC, 10, 5, 14, 0.2, 10, 15, 25) # 28000
    print '==== Формирование цены на собственный товар ===='
    pPDV, pAZ = makeprice(13600, 25, 15, 20)[0:2]
    print '==== Макс. уменьшение цены на свой товар ===='
    minify(13600, pAZ, pPDV, 20)
    print '==== Рассчёт рентабельности ===='
    getprofit(26000, 12, 13600, 15, 20)
