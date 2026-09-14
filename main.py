import os
import sys
import platform
from unittest import case

is_running = True
collection = [ "task1", "task2", "task3", "task4" ]

def system_info():
    print("\n--- Характеристики системы ---")
    print("Операционная система:", platform.system())
    print("Версия ОС:", platform.version())
    print("Архитектура:", platform.architecture()[0])
    print("Процессор:", platform.processor())
    print("Версия Python:", platform.python_version())

print("Добро пожаловать!")
while is_running:
    print("1- осмотреть задачи |\n"
          "2- добавить задачу |\n"
          "3- редактирование задачи |\n"
          "4- удаление задачи |\n"
          "5- характеристики ОС |\n"
          "6- выход |\n")

    choice_user = input("Введите свой выбор")
    match str(choice_user):
        case "1":
            for key, item in enumerate(collection):
                print( key + 1,  item)
        case "2":
            name_task = input("Введите имя задачи")
            collection.append(name_task)
        case '3':
            for key, item in enumerate(collection):
                print(key + 1, item)
            select_edit = int(input("Введите номер задачи для редактирования"))
            edit_name = input("Введите новое название задачи: ")
            collection[select_edit - 1] = edit_name
        case '4':
            for item in enumerate(collection):
                print(key + 1, item)
            delete_edit = int(input("Введите номер задачи для редактирования"))
            collection.pop(delete_edit - 1)
        case "5":
            system_info()
        case "6":
            is_running = False
            print("До свидания!")
        case _:
            print("Такого тут нет!")
