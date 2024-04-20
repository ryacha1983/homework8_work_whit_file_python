import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)

# Функция для переноса по номеру записи:
# def transfer_data(source: str, dest: str, num_row: int):
#     """
#     Функция для переноса указанной строки из одного файла в другой
#     source: str - имя исходного файла
#     dest: str - имя файла куда переносим
#     num_row: int - номер переносимой строки
#     """

#     # with open(source, "r", encoding="utf-8") as file:
#     #     list_1 = file.read().split("\n")
#     # if num_row <= len(list_1):
#     #     with open(dest, "a", encoding="utf-8") as data:
#     #         data.write(list_1[num_row-1] + "\n")
#     # else:
#     #     print("Записи с таким номером нет в указанном файле")

# Функция для переноса записи, по найденному значению:
def transfer_data(source: str, dest: str, record: str):
    """
    Функция для переноса указанной строки из одного файла в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """

    with open(source, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    rez = search_user(source, record)
    if rez != 'По указанному значению совпадений не найдено':
        with open(dest, "a", encoding="utf-8") as data:
            data.write(rez + "\n")
    else:
        print(rez)

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
5 - выход
"""

file = "1.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        source = input("Введите имя файла: ")
        if source not in os.listdir():
            print("указанное имя файла отсутсвует")
            sys.exit()
        else: 
            print(read_all(source))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        source = input("Введите имя исходного файла: ")
        dest = input("Введите имя файла куда переносим: ")
        # Вызов функции для переноса по номеру записи:
        # num_row = int(input("Введите номер записи: "))
        # transfer_data(source, dest, num_row)
        record = input("Введите какую запись необходимо найти и перенести: ")
        transfer_data(source, dest, record)
    elif mode == 5:
        sys.exit()