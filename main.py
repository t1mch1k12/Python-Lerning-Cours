"""
    Точка входа в приложение Task Manager
    version 0.0.5
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
def show_message(message=None, mes_action=None):
    if message is not None:
        print(f" {message} успешно {mes_action} !")
    input("Нажмите ENTER для продолженяи")

def check_confirm(action: str):
    confirm = input("  Да / Нет")
    if not(confirm.startswith('y')
            or confirm.startswith('Y')):
        print(action)
        return False
    else:
        return True

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
            show_message()
        case '2':
            add_task = input("Введите имя задачи для добавления")
            collection.append(add_task)
            show_message(add_task, "добавлена")
        case '3':
            show_collection(collection)
            select_task = int(input("Введите номер задачи"))
            edit_task = input("Введите новое имя задачи для редактирования")
            collection[select_task - 1] = edit_task
            show_message(edit_task, "переименована")
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления"))
            if check_confirm("Удаление прошло успешно!"):
                collection.pop(delete_task - 1)
                show_message(delete_task, "удалена")
        case '5':
            is_running = check_confirm("До свидания!")
        case _:
            print("Такого пункта нет!")






