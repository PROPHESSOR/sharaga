# Человеко-машинный интерфейс

Литература:
- «Навчальний посiбник з дисциплiни Людинно-машинний iнтерфейс» Уткiна 
- Головач В.В. «Дизайн пользовательского интерфейса. Искусство мыть слона»

*03.02.2020*

## Общая характеристика программных систем

### Информационная система как вид программной системы

**Информационная система** (ИС) - это человеко-машинная система, которая собирает, хранит, обрабатывает и выдаёт по запросу информацию.
Так же, это система, которая обеспечивание выработку решений на основе автоматизации информационных процессов в разных сферах человеческой деятельности.

Программа «Домашний доктор».

Функции ИС - это совокупность действий, направленная на достижения поставленной цели.

По способу деятельности различают:
- По масштабу
  - Одиночные (на одном компьютере)
  - Групповые (используются группой человек как локальная вычислительная сеть)
  - Корпоративные (имеют иерархическую структуру, используют интернет для работы )
- По типам пакетов (типы пакетной передачи)
  - *OLDP (регулярный интенсивный поток данных)*
- По функциям управления
  - Управление текстом
  - Управление графикой
  - Управление программами
  - Управление HTML
- По типу интерфейса
  - Командный
  - Поисковой системы (может включать голос)
  - Графический

### Понятие интерфейса и виды интерфейсов

Интерфейс - правило взаимодействия программ с пользователем и другими программами.

В зависимости от взаимодействия, различают несколько видов интерфейсов:
- Командный
- Оконный (графический) (WIMP)
- Языковой *tongue* (SILK)

Каждый из видов интерфейсов требует определённой структуры реализации.

**Технология** - комплекс научных и инженерных знаний, реализрованых в наборе технических, материальных и трудовых факторах производства, которые используются для разработки определённого продукта.

Некоторые технологии:
- Пакетная технология (перфокарты и пакеты байтов)
- Технология командной строки
- Графический интерфейс
- Языковая технология (сер. 90-х) - Голосовые команды
- Биометрическая технология (начало 20k-х)

<!-- Мы что, блин, третий раз пишем одно и то же?! =D -->

*06.02.2020*

Интерфейсы пользователя:
- Процедурно-ориентированный
  - Примитивный — организовывают взаимодействие с пользователем в консольном режиме <!-- Рили? :/ -->
  - С меню — позволяет пользователю выбирать операции из списка
    - Одноуровневые
    - Иерархические
  - Со свободной навигацией (Графический) — ориентированы на выполнение задания в графическом режиме
- Объектно-ориентированный
  - Интерфейс прямого манипулирования — предполагает, что взаимодействие с пользователем происходит с помощью выбора и перемещения пиктограм

#### Пример

Разработать пользовательский интерфейс для наглядной демонстрации графика функции y = f(x).
Программа должна рассчитывать и строить график функции.

##### Примитивный

```
[ Название        _[]X]
| Функция: [      ]   |
| Знач. X: [      ]   | // Enter для построения графика
|                     |
|     [ .     ]       |
|     | .     |       |
|     [ ..... ]       |
|                     |
[                     ]
```

##### Одноуровневое меню

<?xml version="1.0" standalone="no"?><svg width="640" height="480"><defs><clipPath id="_clipPath"><rect width="640" height="480"/></clipPath></defs><g clip-path="url(#_clipPath)"><rect x="115.5" y="106.75" width="409" height="295.5" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="1" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="115.5" y="77.75" width="409" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(217,217,217)" stroke-width="1" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><g><rect x="466.5" y="77.75" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(7,159,215)"/><g transform="matrix(1,0,0,1,470.5,77.75)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-size:20px;fill:#000000;stroke:none;">[ ]</text></g></g><g><rect x="437.5" y="77.75" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(151,151,151)"/><g transform="matrix(1,0,0,1,446.5,77.75)"><text transform="matrix(1,0,0,1,0.039,21.377)" style="font-size:20px;fill:#000000;stroke:none;">_</text></g></g><g><rect x="495.5" y="77.75" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(255,0,0)"/><g transform="matrix(1,0,0,1,504.5,77.75)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-size:20px;fill:#000000;stroke:none;">X</text></g></g><rect x="124.5" y="120.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="124.5" y="155.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="124.5" y="186.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="264.5" y="120.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="264.5" y="155.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="264.5" y="186.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="399" y="120.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="399" y="155.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="399" y="186.75" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="2" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><rect x="180" y="224.75" width="267.5" height="167" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" stroke-width="1" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><g><line x1="222.5" y1="267.75" x2="222.5" y2="367.75" stroke-width="1" stroke="rgb(0,0,0)" stroke-miterlimit="3"/><line x1="222.5" y1="367.75" x2="405.5" y2="367.75" stroke-width="1" stroke="rgb(0,0,0)" stroke-miterlimit="3"/></g><g transform="matrix(1,0,0,1,129,123.25)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Функция</text></g><g transform="matrix(1,0,0,1,129,158.079)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g><g transform="matrix(1,0,0,1,129,190.058)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g><g transform="matrix(1,0,0,1,269,123.25)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Отрезок</text></g><g transform="matrix(1,0,0,1,269,158.079)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g><g transform="matrix(1,0,0,1,269,190.058)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g><g transform="matrix(1,0,0,1,403.5,123.25)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Шаг</text></g><g transform="matrix(1,0,0,1,403.5,158.079)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g><g transform="matrix(1,0,0,1,403.5,190.058)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-size:12px;fill:#000000;stroke:none;">Бла</text></g></g></svg>

##### Интерфейс со свободной навигацией

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate" viewBox="0 0 640 480" width="640" height="480"><defs><clipPath id="_clipPath_WxvWIIb9k3Vjrz4NSjK4O46udt3SZbif"><rect width="640" height="480"/></clipPath></defs><g clip-path="url(#_clipPath_WxvWIIb9k3Vjrz4NSjK4O46udt3SZbif)"><rect x="37.5" y="133" width="565" height="243" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="37.5" y="104" width="565" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(217,217,217)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g><rect x="544.5" y="104" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(7,159,215)"/><g transform="matrix(1,0,0,1,548.5,104)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">[ ]</text></g></g><g><rect x="515.5" y="104" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(151,151,151)"/><g transform="matrix(1,0,0,1,524.5,104)"><text transform="matrix(1,0,0,1,0.039,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">_</text></g></g><g><rect x="573.5" y="104" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(255,0,0)"/><g transform="matrix(1,0,0,1,582.5,104)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">X</text></g></g><rect x="120.5" y="147" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="260.5" y="147" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="50" y="200.786" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="474.5" y="272.5" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="50" y="242.214" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="474.5" y="313.927" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="395" y="147" width="111" height="21" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="191" y="189" width="267.5" height="167" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g><line x1="233.5" y1="232" x2="233.5" y2="332" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><line x1="233.5" y1="332" x2="416.5" y2="332" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/></g><g transform="matrix(1,0,0,1,127.5,147.286)"><text transform="matrix(1,0,0,1,0,16.033)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:15px;font-style:normal;fill:#000000;stroke:none;">Функция</text></g><g transform="matrix(1,0,0,1,398.5,147.573)"><text transform="matrix(1,0,0,1,0,16.033)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:15px;font-style:normal;fill:#000000;stroke:none;">Шаг</text></g><circle vector-effect="non-scaling-stroke" cx="0" cy="0" r="1" transform="matrix(8,0,0,8,490.5,208)" fill="rgb(235,235,235)" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><circle vector-effect="non-scaling-stroke" cx="0" cy="0" r="1" transform="matrix(8,0,0,8,490.5,233)" fill="rgb(235,235,235)" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g transform="matrix(1,0,0,1,509.5,197)"><text transform="matrix(1,0,0,1,0,16.033)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:15px;font-style:normal;fill:#000000;stroke:none;">График</text></g><g transform="matrix(1,0,0,1,509.5,221.786)"><text transform="matrix(1,0,0,1,0,16.033)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:15px;font-style:normal;fill:#000000;stroke:none;">Таблица</text></g></g></svg>

##### Интерфейс прямого манипулирования

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate" viewBox="0 0 640 480" width="640" height="480"><defs><clipPath id="_clipPath_nD1X0pJvvhMtuui8WApPxFZGhCoqP9Ik"><rect width="640" height="480"/></clipPath></defs><g clip-path="url(#_clipPath_nD1X0pJvvhMtuui8WApPxFZGhCoqP9Ik)"><rect x="115.5" y="119" width="409" height="271" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><rect x="115.5" y="90" width="409" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(217,217,217)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g><rect x="466.5" y="90" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(7,159,215)"/><g transform="matrix(1,0,0,1,470.5,90)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">[ ]</text></g></g><g><rect x="437.5" y="90" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(151,151,151)"/><g transform="matrix(1,0,0,1,446.5,90)"><text transform="matrix(1,0,0,1,0.039,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">_</text></g></g><g><rect x="495.5" y="90" width="29" height="29" transform="matrix(1,0,0,1,0,0)" fill="rgb(255,0,0)"/><g transform="matrix(1,0,0,1,504.5,90)"><text transform="matrix(1,0,0,1,0,21.377)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:20px;font-style:normal;fill:#000000;stroke:none;">X</text></g></g><g><rect x="149.5" y="130" width="39" height="39" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g transform="matrix(1,0,0,1,134,174.658)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:12px;font-style:normal;fill:#000000;stroke:none;">Компьютер</text></g></g><g><rect x="262.25" y="130" width="39" height="39" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g transform="matrix(1,0,0,1,235.75,174.658)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:12px;font-style:normal;fill:#000000;stroke:none;">Чистые бланки</text></g></g><g><rect x="463.5" y="130" width="39" height="39" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g transform="matrix(1,0,0,1,458,174.658)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:12px;font-style:normal;fill:#000000;stroke:none;">Корзина</text></g></g><g><rect x="374" y="130" width="39" height="39" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="2" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g transform="matrix(1,0,0,1,358.5,174.658)"><text transform="matrix(1,0,0,1,0,12.826)" style="font-family:&quot;Open Sans&quot;;font-weight:400;font-size:12px;font-style:normal;fill:#000000;stroke:none;">Картотека</text></g></g><rect x="180" y="212" width="267.5" height="167" transform="matrix(1,0,0,1,0,0)" fill="rgb(235,235,235)" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><g><line x1="222.5" y1="255" x2="222.5" y2="355" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/><line x1="222.5" y1="355" x2="405.5" y2="355" vector-effect="non-scaling-stroke" stroke-width="1" stroke="rgb(0,0,0)" stroke-linejoin="miter" stroke-linecap="square" stroke-miterlimit="3"/></g></g></svg>

### Специфика информационных систем
### Основные задание ИС


## Способы (правила) проектировани интерфейса <!-- Засади проектування ... -->

### Психофизические передумови взаимодействия человека и компьютера

При проектировании интерфейса необходимо учитывать психические и физиологические особенности человека, связанные с восприятием, запоминанием и обработкой информации

Виды памяти:
- Краткосрочная
- Долгосрочная

Восприятие цвета

Восприятие звука

### Програмная модель пользовательского интерфейса

Программная модель восприятия пользователя и программиста

Модели восприятия пользовательских интерфейсов:
- Программиста
- Пользователя — это совокупность обобщённых представлений конкретного пользователя или группы пользователей про процессы, происходящие внутри программы и базируется на опыте конкртеных пользователей.
- Программная

Характеристики...

### Критерии оценивания интерфейса пользователя

Существуют 4 основных критерия оценки:
- Скорость работы пользователя
  - Основной метод оценки скорости — **GOMS**, разработанный в 1983г. Оценивает цели, методы и правила по работе пользователя.
    - Идея метода в том, чтобы все действия пользователя можно было разложить на составляющие
    - Был улучшен в виде метода KLM
- Количество человеческих ошибок
- Скорость обучения
- Субъективное удовлетворение пользователя

#### Скорость выполнения работы

| Тип действия | Длительность (с) | Комментарий |
| --- | --- | --- |
| Д | 62 | Анализ |
| П | 1.1 | Перемещение мыши |
| М | 0.1 | Нажатие на кнопку мыши |
| В | 0.4 | Взятие/отпускание мыши |

...


##### Задача

Рассчитать и представить в таблице разными операциями сохранение документа в активной папке под именем class и выйти из программы.

Чайник

| Тип действия | Длительность (с) | Комментарий |
| --- | --- | --- |
| Д | 62  | Анализ |
| П | 1.1 | Перемещение мыши |
| М | 0.1 | Нажатие на кнопку мыши |
| Д | 1.1 | Ищет кнопку "Сохранить" |
| М | 0.1 | Нажатие на кнопку мыши |
| Р | 0.1 | Отклик системы |
| Д | 1.1 | Ищет кнопку "Сохранить" |
| П | 0.1 | Отклик системы |


Взаимодействие пользователя с системой состоит из следующих основных шагов (7):
- Формирование цели действия
- Определение общей направленности действия (алгоритм)
- Определение конкретных действий
- Выполнение определённых действий
- Восприятие нового состояния системы
- Интерпретация состояния системы
- Оценка результата

Анализируя примеры можна выделить определённые требования к человеку:
- Что он хочет получить на выходе
- Как минимум, одна успешная последовательность действий, что приводит к результату
- Где найти необходимые объекты для выполнения
- Как определить пригодность объектов для использования
- Как взаимодействовать с объектом

Для решения проблем 2-5 существует единственное решение, которое называется **непосредственным манипулированием**.

Смысл этого метода лежит в том, что пользователь не отдаёт команды, а манипулирует объектами

Важность при создании интерфейса в том, чтобы максимально упростить возвращение пользователей от одного действия к другому, чтобы пользователь минимально об этом задумывался

При этом, пользователь должен знать:
- На каком шаге он остановился
- Какие команды/параметры он уже ввёл
- Что именно он должен сделать на текущем шаге
- На что было обращего его внимание на предыдущем шаге

Длительность физических действий зависит от степени автоматизации работы и степени необходимой точности работы (скорость/качество)

```
ВремяДостиженияЦели = парам1 + парам2 * log2(ДистанцияОтКурсораДоЦели[px]/РазмерЦели[px]+1) [мм*с]
```

#### Что такое человеческие ошибки

Эффективность интерфейса основным образом зависит от тех ошибок, которых допускает пользователь во время его использования.

Термин человеческой ошибки возникает в двух случаях:
- Люди в ошибках системы склонны винить себя
- Существующее положение вещей выгодно руководству

#### Типы ошибок
