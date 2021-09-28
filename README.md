# Генераторы бейджей для конференции ВЗМШ

Инструкция использования генераторов бейджей участников и организаторов для конференции ВЗМШ.

## Содержание

- [Генераторы бейджей для конференции ВЗМШ](#генераторы-бейджей-для-конференции-взмш)
  - [Содержание](#содержание)
  - [1. Принцип работы генератора бейджей для участников](#1-принцип-работы-генератора-бейджей-для-участников)
    - [1.1 Запуск генератора генератора бейджей для участников](#11-запуск-генератора-генератора-бейджей-для-участников)
    - [1.2 Описание работы генератора бейджей для участников](#12-описание-работы-генератора-бейджей-для-участников)
  - [2 Принцип работы генератора бейджей для организаторов](#2-принцип-работы-генератора-бейджей-для-организаторов)
    - [2.1 Запуск генератора генератора бейджей для организаторов](#21-запуск-генератора-генератора-бейджей-для-организаторов)
    - [2.2 Описание работы генератора бейджей для организаторов](#22-описание-работы-генератора-бейджей-для-организаторов)
  - [3 Возможные проблемы в работе генераторов бейджей](#3-возможные-проблемы-в-работе-генераторов-бейджей)

## 1. Принцип работы генератора бейджей для участников

### 1.1 Запуск генератора генератора бейджей для участников

Команда запуска:
- Для Linux: `python3 gen_partics.py`
- Для Windows: `py gen_partics.py`

Необходимые файлы и папки для работы:

| Название файла или папки    | Описание                                  |
| --------------------------- | ----------------------------------------- |
| `./list_partics.txt`        | Файл данных для подстановки в шаблон      |
| `./input/participants.fodg` | Шаблон бейджа участника                   |
| `./output`                  | Папка для сгенерированного файла бейдежей |

### 1.2 Описание работы генератора бейджей для участников

Генератора бейджей для участников ищет шаблон `participants.fodg` в папке `input`. После замены на данные из файла `list_partics.txt`,
генератор формирует файл `auto_participants.fodg` в папку `output`.

Генератор бейджей для участников заменяет даннные по следующему принципу:

| Название поля        | Обязательное поле? | Описание           |
| -------------------- | :----------------: | ------------------ |
| `participsurname`    |       **+**        | Фамилия участника  |
| `participname`       |       **+**        | Имя участника      |
| `particippatronymic` |       **+**        | Отчество участника |
| `participcity`       |       **+**        | Город участника    |

Данные для подстановки в шаблон имеют вид, как на данном примере:
```
Иванов Иван Иванович Москва
Васильев Василий Васильевич Ростов-на-Дону
Петров Петр Петрович Старый Оскол
```

## 2 Принцип работы генератора бейджей для организаторов

### 2.1 Запуск генератора генератора бейджей для организаторов

Команда запуска:
- Для Linux: `python3 gen_orgs.py`
- Для Windows: `py gen_orgs.py`

Необходимые файлы для работы:

| Название файла или папки | Описание                                  |
| ------------------------ | ----------------------------------------- |
| `./list_orgs.txt`        | Файл данных для подстановки в шаблон      |
| `./input/orgs.fodg`      | Шаблон бейджа организатора                |
| `./output`               | Папка для сгенерированного файла бейдежей |

### 2.2 Описание работы генератора бейджей для организаторов

Генератора бейджей для организаторов ищет шаблон `orgs.fodg` в папке `input`. После замены на данные из файла `list_orgs.txt`,
генератор формирует файл `auto_orgs.fodg` в папку `output`.

Генератор бейджей для организаторов заменяет даннные по следующему принципу:

| Название поля   | Обязательное поле? | Описание              |
| --------------- | :----------------: | --------------------- |
| `orgsurname`    |       **+**        | Фамилия организатора  |
| `orgname`       |       **+**        | Имя организатора      |
| `orgpatronymic` |       **+**        | Отчество организатора |

Данные для подстановки в шаблон имеют вид, как на данном примере:
```
Иванов Иван Иванович
Васильев Василий Васильевич
Петров Петр Петрович
```

## 3 Возможные проблемы в работе генераторов бейджей
- Количество бейджиков в шаблоне из папки `input` должно быть больше, чем позиций (строк) в файле данных. Иначе возможны ошибки.
- Грода в два слова обрабатываются корректно, но через костыль `:(` (Старый Оскол, Нижний Новгород, etc).
