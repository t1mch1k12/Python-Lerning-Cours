"""
    --- description ---
    - [x] создать репозиторий проекта
    - [x] реализовать цикл приложения
    - [] реализовать хранилище задач
"""
from unittest import case

is_running = True
collection = []

print("Добро пожаловать!")
while is_running:
    print("1- осмотреть задачи |\n"
          "2- добавить задачу |\n"
          "3- редактирование задачи |\n"
          "4- удаление задачи |\n"
          "5- выход |\n")
    choice_user = input("Введите свой выбор")
    match choice_user:
        case "1":
            for item in enumerate(collection):
                print( key + 1,  item)
        case "2":
            name_task = input("Введите имя задачи")
            collection.append(name_task)
        case '3':
            for item in enumerate(collection):
                print(key + 1, item)
            select_edit = int(input("Введите номер задачи для редактирования"))
            collection[select_edit - 1] = edit_name
        case '4':
            for item in enumerate(collection):
                print(key + 1, item)
            delete_edit = int(input("Введите номер задачи для редактирования"))
            collection.pop(delete_edit - 1)
        case "5":
            is_running = False
            print("До свидания!")
        case _:
            print("Такого тут нет!")

