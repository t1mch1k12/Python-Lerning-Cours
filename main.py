"""
    Точка входа в приложение Task Manager
    version 0.0.4
    --- description ---
    проложение может сохранять задачи,
    редактировать, выдает список задач
    и может удалять задачу.
"""
"""функция выводит список в консоль"""
def show_collection(task_list):
    print("~" * 30)
    for i, j in enumerate(task_list):
        print(i + 1, j)
    print("~" * 30)

"""функция выводит уведомления в консоль"""
def show_massage(flag: bool ,massage=None):
    if not flag:
        print(f"Новая задача {massage} успешно добавлена!")
    input("Нажмите ENTER для продолженяи")

is_running = True
collection = ["task 1", "task 2"] # list

print("Добро пожаловать!")
while is_running:
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактирование задачи \n"
          "4 - удаление задачи \n"
          "5 - выход")

    choice_user = input("Введите свой выбор")
    match str(choice_user):
        case '1':
            show_collection(collection)
            show_massage(False)
        case '2':
            add_task = input("Введите имя задачи для добавления")
            collection.append(add_task)
            show_massage(add_task)
        case '3':
            show_collection(collection)
            select_task = int(input("Введите номер задачи"))
            edit_task = input("Введите новое имя задачи для редактирования")
            collection[select_task - 1] = edit_task
            print(f"{edit_task} успешно переименована!")
            input("Нажмите ENTER для продолженяи")
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления"))
            collection.pop(delete_task - 1)
            print(f"-> {delete_task} успешно удалена!")
            input("Нажмите ENTER для продолженяи")
        case '5':
            is_running = False
            print("До свидания!")
        case _:
            print("Такого пункта нет!")






