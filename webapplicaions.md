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

