#В ежедневник можно добавлять задачи, которые необходимо выполнить. Другими словами это планировщик задач или органайзер.

#Каждая задача должна иметь:
#- уникальный идентификатор
#- название
#- текст задачи
#- запланированное время выполнения

#Программа должна проверять вводимые пользователем данные. Например, если
#уникальный идентификатор не является целым числом или не существует в БД,
#то нужно выводить сообщение об ошибке. Подумайте, какие еще данные, вам нужно проверять.

#Главное меню программы:
#1. Вывести список задач
#Выводит список всех задач со статусом выполнения за указанный день. По-умолчанию, выводит за текущий день.
#2. Добавить задачу
#Добавить новую задачу в указанное время.
#3. Отредактировать задачу
#Для редактирования задачи используется уникальный идентификатор в БД. Если задача не найдена, то нужно вывести ошибку.
#4. Завершить задачу
#Меняет статус задачи на "Выполнено"
#5. Начать задачу сначала
#Меняет статус задачи на "Не выполнено"
#6. Выход


from datetime import datetime, date, time

import sys #exit

from task_organizer import storage_org

conn = storage_org.connect()
storage_org.initialize(conn)


def action_show_menu():
    print('''
Ежедневник.
m - показать меню
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выйти''')

def tasklist():
    print('Список задач на сегодня:')
    print(storage_org.find_all(conn))

    def add_task():
        name = input('\n.Добавьте новую задачу. Введите название: ')
        description = input('Введите описание: ')
        dt_task= timefunction()

        new_task = {
            'task_name': name,
            'task_edit': description,
            'task_time': dt_task
        }

        storage_org.add_task_full(conn, new_task)

def edit_task():

    print('Редатирование задачи.Введите номер задачи, которая будет отредактирована:')

    pk = int(input)

    print('Текущая версия задачи:\n', storage_org.find_task_by_pk(conn, pk))

    name = input('\nВведите новое название: ')
    description = input('Введите новое описание: ')
    dt_task = timefunction()

    new_task = {
        'task_name': name,
        'task_edit': description,
        'task_time': dt_task
    }

storage_org.change_task(conn, task_name, pk)


def end_task():
    print ('Какую задачу вы хотите завершить?. Введите номер задачи:')
    pk = int(input('\nВведите номер задачи: '))
    storage_org.change_status(conn, task_status, pk, 1)
    print('Вы отметили задачу № {} как выполненную'.format(pk))




def again_task():
    print('Какую задачу вы хотите начать сначала? Введите номер задачи:')
    pk = int(input('\nВведите номер задачи: '))
    storage_org.change_status(conn, task_status, pk, 0)
    print('Вы отметили задачу № {} как невыполненную'.format(pk))



def action_exit():
    sys.exit(0)

actions = {
    'm': action_show_menu(),
    '1':tasklist,
    '2':add_task,
    '3':edit_task,
    '4':end_task,
    '5':again_task,
    '6': action_exit,
}

if __name__ == '__main__':
    action_show_menu()

    while True:
         cmd = input('\nВведите команду:')
         action = actions.get(cmd)  # вызываем значение из словаря с помощью гет.

         if action:
             action()
         else:
             print('Неизвестная команда')


def timefunction():
    while True:
        st = input('Введите данные в формате yyyy-mm-dd hh-mm: ')
        dt = datetime.datetime(
                         year=int(st[0:4]),
                         month=int(st[5:7]),
                         day=int(st[8:10]),
                         hour=int(st[11:13]),
                         minute=int(st[14:16])
                     )
        return dt






#a = datetime.today()
#print('Сегодня', a,'.','На какую дату и время вы хотите назначить задачу?:')

#user_data = input('*введите данные формате dd/mm/yy 00:00. Например: 21/11/06 16:30 \n')
#user_data = datetime.strptime(user_data,"%d/%m/%y %H:%M")
#user_data = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")









#print(
 #   'Ежедневник. Выберите действие:','\n',
#'1. Вывести список задач','\n',
#'2. Добавить задачу','\n',
#'3. Отредактировать задачу','\n',
#'4. Завершить задачу','\n',
#'5. Начать задачу сначала','\n',
#'6. Выход'
#       )

#n = int(input())

#if 1>n or n>6 :
#    print('Номер действия задан неверно. Выберите действие под номером от 1 до 6:')
#if n == 1:
#    print('Список задач:')

#if n == 2:
 #   print('Добавьте задачу:')
#id

#a = datetime.today()
#print('Сегодня', a,'.','На какую дату и время вы хотите назначить задачу?:')

#user_data = input('*введите данные формате dd/mm/yy 00:00. Например: 21/11/06 16:30 \n')
#user_data = datetime.strptime(user_data,"%d/%m/%y %H:%M")
#user_data = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

#print('На какое время назначить задачу?')
#print(datetime.now())

#datetime.today()# объект datetime из текущей даты и времени.
#datetime.strptime(date_string, format) #преобразует строку в datetime (так же, как и функция strptime из модуля time).
#date
#datetime.time
#a = datetime.now().minute
#if n == 3:
#    print('Редатирование задачи.Введите ')

#if n == 4:
#    print('Какую задачу вы хотите завершить?. Введите ID задачи:')

#if n == 5:
 #   print('Какую задачу вы хотите начать сначала? Введите ID задачи:')

#if n == 6:
  #  print('До встречи!')


#list = []
#print(list)


