'''
Линейная алгебра
'''

'''
### Комплексные числа

Зачем?
- x^2 = -1 like x^2 = 2
- Сжатие во фракталах


N -> Z -> Q -> R -> C - Наследование множеств
N: >0
Z: int


Комплексное число  - упорядоченное множество (x, y): x - R, y - I

(x, 0) - R

(x, y) - Воображаемые числа
(0, 0) - "ноль"

Мощность множества - length

z1 + z2 = (x1 + x2, y1 + y2)
z1 - z2 = (x1 - x2, y1 - y2)
z1 * z2 = ([x1 * x2] - [y1 * y2], [x1 * y2] + [x2 * y1])
z1 / z2 = ([(x1 * x2 + y1 * y2) / x2 ^ 2 + y2 ^ 2], [(x2 * y1 - x1 * y2) / (x2^2 + y2^2)]

Последствия:
- minus
- div

## Алгебраическая форма C

i = (0, 1) // Воображаемая единица
i^2 = -1 // (0, 1) * (0, 1) = -1
i != sqrt(-1)! // ±

z = (x, y) = (x, 0) + (0, y) = (x, 0) + (0, 1) * (y, 0) = x + iy = x + yi

z¯ = x - iy // Обёрнутое "спряжене"

z*z¯ = x^2+y^2 in R
z+z¯ = 2 * x in R

(x-3i)(5+i) = 2*2 + 2i - 3i*5 - 3i² = 10 + 2i - 15i +3=13-13i

i^3 = i * i^2 = -i
i^4 = i^2^2 = 1
i^5 = i


'''

class Complex():
    def __init__(self, x, y=0):
        self.x, self.y = x, y

    def __add__(self, self2):
        return Complex(self.x + self2.x, self.y + self2.y)

    def __sub__(self, self2):
        return Complex(self.x - self2.x, self.y - self2.y)

    def __mul__(self, self2):
        return Complex(self.x * self2.x - self.y * self2.y, self.x * self2.y + self2.x * self.y)

    def __div__(self, self2):
        return Complex(
                (self.x * self2.x + self.y * self2.y) / (self2.x**2 + self2.y**2),
                (self2.x * self.y - self.x * self2.y) / (self2.x**2 + self2.y**2)
        )

    def __str__(self):
        if self.y == 0:
            return str(self.x)
        else:
            return f'{self.x if self.x != 1 else ""}{"+" if self.y >= 0 else ""}{self.y if self.y != 1 else ""}i'
