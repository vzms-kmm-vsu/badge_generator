# Генераторы бейджей для конференции ВЗМШ

## Содержание

- [Генераторы бейджей для конференции ВЗМШ](#генераторы-бейджей-для-конференции-взмш)
  - [Содержание](#содержание)
  - [1. Принцип работы генератора бейджей для участников](#1-принцип-работы-генератора-бейджей-для-участников)
    - [1.1 Запуск генератора бейджей для участников](#11-запуск-генератора-бейджей-для-участников)
    - [1.2 Описание работы генератора бейджей для участников](#12-описание-работы-генератора-бейджей-для-участников)
  - [2 Принцип работы генератора бейджей для организаторов](#2-принцип-работы-генератора-бейджей-для-организаторов)
    - [2.1 Запуск генератора бейджей для организаторов](#21-запуск-генератора-бейджей-для-организаторов)
    - [2.2 Описание работы генератора бейджей для организаторов](#22-описание-работы-генератора-бейджей-для-организаторов)
  - [3 Возможные проблемы в работе генераторов бейджей](#3-возможные-проблемы-в-работе-генераторов-бейджей)

## 1. Принцип работы генератора бейджей для участников

### 1.1 Запуск генератора бейджей для участников

Команда запуска:
- Для Linux: `python3 gen_partics.py`
- Для Windows: `py gen_partics.py`

Необходимые файлы и папки для работы:

| Название файла или папки    | Описание                                 |
| --------------------------- | ---------------------------------------- |
| `./list_partics.csv`        | Файл данных для подстановки в шаблон     |
| `./input/participants.fodg` | Шаблон бейджа участника                  |
| `./output`                  | Папка для сгенерированного файла бейджей |

### 1.2 Описание работы генератора бейджей для участников

Генератор ищет шаблон `participants.fodg` в папке `input`. После замены на данные из файла `list_partics.csv`,
генератор формирует файл `auto_participants.fodg` в папку `output`.

Генератор заменяет данные по следующему принципу:
| Имя переменной в шаблоне | Название поля | Описание           |
| ------------------------ | :-----------: | ------------------ |
| `participsurname`        |   `surname`   | Фамилия участника  |
| `participname`           | `patronymic`  | Имя участника      |
| `particippatronymic`     |    `name`     | Отчество участника |
| `participcity`           |    `city`     | Город участника    |

Данные для подстановки в шаблон имеют вид, как на данном примере:
```
surname;name;patronymic;city
Иванов Иван Иванович Москва
Васильев Василий Васильевич Ростов-на-Дону
Петров Петр Петрович Старый Оскол
```

## 2 Принцип работы генератора бейджей для организаторов

### 2.1 Запуск генератора бейджей для организаторов

Команда запуска:
- Для Linux: `python3 gen_orgs.py`
- Для Windows: `py gen_orgs.py`

Необходимые файлы для работы:

| Название файла или папки | Описание                                 |
| ------------------------ | ---------------------------------------- |
| `./list_orgs.csv`        | Файл данных для подстановки в шаблон     |
| `./input/orgs.fodg`      | Шаблон бейджа организатора               |
| `./output`               | Папка для сгенерированного файла бейджей |

### 2.2 Описание работы генератора бейджей для организаторов

Генератор ищет шаблон `orgs.fodg` в папке `input`. После замены на данные из файла `list_orgs.csv`,
генератор формирует файл `auto_orgs.fodg` в папку `output`.

Генератор заменяет данные по следующему принципу:
| Имя переменной в шаблоне | Название поля | Описание              |
| ------------------------ | :-----------: | --------------------- |
| `participsurname`        |   `surname`   | Фамилия организатора  |
| `participname`           | `patronymic`  | Имя организатора      |
| `particippatronymic`     |    `name`     | Отчество организатора |


Данные для подстановки в шаблон имеют вид, как на данном примере:
```
surname;name;patronymic
Иванов Иван Иванович
Васильев Василий Васильевич
Петров Петр Петрович
```

## 3 Возможные проблемы в работе генераторов бейджей
- Количество бейджиков в шаблоне из папки `input` должно быть больше, чем позиций (строк) в файле данных. Иначе возможны ошибки.
