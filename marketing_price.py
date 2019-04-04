#!/usr/bin/python
# coding: utf-8

def percent(x):
    return float(x) / 100.0

def calculate(KB, TBp, BPp, CMp, duty, OMPp, AZp, overprice, USD=27.06, PDVp=20):
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

if __name__ == "__main__":
    calculate(912, 10, 5, 14, 0.2, 10, 15, 25)
