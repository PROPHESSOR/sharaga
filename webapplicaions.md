# Конспект по дисциплине WEB-приложение

Сервера:
- Apache
- Nginx
- IIS
- TomCat

DevOps - системные администраторы.

DOU.UA

## Тема: Формы HTML

Форма - это какой-то элемент, который служит для ввода информации с целью её дальнейшей обработки.


@media
- speech        - Для слепых
- handler       - Сенсорные устройства
- print         - При печати
- projection    - При выводе на проектор
- screen        - Для мониторов


```css

@media handler {
    /* For tablets and phones */
}

@media screen {
    /* For desktop */
}

```

```
mysqli($databasename, $login, $password);
mysqli->query($connect, $query);

```


```
CREATE TABLE books(
    VARCHAR(32) author,
    VARCHAR(32) title,
) ENGINE MyISAM;

```

Команды:
- CREATE
- ALTER (изменить в таблице)
- DELETE (удаление строки)
- DROP (удаление таблицы)
- DESCRIBE (структура таблицы в админконсоль)
- GRANT (изменения прав пользователя)
- BACKUP
- UPDATE
- SELECT
- INSERT
- LOCK (блокирование записи или таблицы: LOCK TABLE)
- UNLOCK
- SHOW (урезанная версия DESCRIBE)
- TRUNCATE (очищает таблицу)
- USE (задаёт контекст)
- RENAME


Типы данных:
- CHAR < 255
- VARCHAR < 65536
- TEXT 64k
- TINYTEXT < 256
- MEDIUMTEXT 16M
- LONGTEXT 4G
- BINARY (небольшие картинки)
- VARBINARY < 64k
- BLOB (Binary Large OBject)
- TINYBLOB
- MEDIUMBLOB
- LONGBLOB

```
$fileStream = fopen('path', rwa) // Для совместимости a+, w+ = a
```

```
while (!feof($fileStream)) {
    $str = fgets($fileStream);
    echo $str . '<br/>';
}

```


- fopen(path, mode) - Открывает поток файла
- fgets(stream) - Читает строку для EOL
- fgetc(stream) - Читает символ
- fwrite(path, string) - Записать строку в файл (перезаписывает)
  - \n - Перенос строки
  - \r - Возврат коретки
  - \t - Табуляция
- fsize(path) - Размер файла в байтах
- fclose(path) - Закрыть файл. Частая причина торможения работы сервера.
- file\_get\_contents - Считать файл в String переменную.

## Cookies

- setcookie(name, value, [expire {time() + 60 \* 60 \* 24 \* 30}, path, domain, !!secure, !!httponly])

```isset($_SERVER['PHP_AUTH_USER']) && isset($_SERVER['PHP_AUTH_PW'])```

- md5 - HEX x32
- sha1 - HEX x40
- sha2 - HEX x40
- hash('ripe128', value) - x32
