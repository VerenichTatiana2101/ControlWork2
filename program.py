import os
import uuid
import csv
from datetime import datetime

# готов
def add_note(file_name):
    names = ["ID", " заголовок", " заметка", " дата"]
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(
            w_file, delimiter=';', lineterminator='\n', fieldnames=names)
        if not file_exists:
            file_writer.writeheader()
        title = input('Введите заголовок заметки: ').title()
        body = input('Введите тело заметки: ')
        if not title.strip() or not body.strip():
            print('Заголовок или тело заметки не могут быть пустыми!')
        else:
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            note_id = str(uuid.uuid4())
            file_writer.writerow(
                {"ID": note_id, " заголовок": title, " заметка": body, " дата": date})
            print('Заметка успешно добавлена!')
    input('Нажмите любую клавишу для продолжения работы')

# готов, просто показывает весь список по дате изменения
def show_notes(file_name):
    try:
        with open(file_name, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=';')
            count = 0

            for row in file_reader:
                if count == 0:
                    print(";".join(row))
                else:
                    print(row[0], row[1], row[2], row[3])
        with open(file_name, 'r') as file:
            data = file.readlines()
        input('\npress any key')
    except FileNotFoundError:
        print('Файл не найден')
        input('\npress any key')

# готово, добавить изменение заголовка
def rename_note(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        title = input('Введите заголовок заметки: ').title()
        notes = []
        for row in reader:
            if title in row[1]:
                new_body = input('Введите тело заметки: ')
                if not new_body.strip():
                    print('тело заметки не может быть пустым!')
                else:
                    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    row[2] = new_body
                    row[3] = date
                    print('Заметка успешно добавлена!')
            notes.append(row)
    with open(file_name, mode='w', newline='', encoding='utf-8') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(notes)
    input('Нажмите любую клавишу для продолжения работы')

# готов, ограничить отсутствие ввода
def search_note(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        title = input('Введите заголовок заметки: ').title()
       
        for row in reader:
            if title in row[1]:
                print(row)
                break
        else:
            print('нет заметки с данным заголовком.')
    input('нажмите любую клавишу')

# готов
def drawing():
    print('1 - показать заметки')
    print('2 - добавить заметку')
    print('3 - найти заметку')
    print('4 - удалить заметку')
    print('5 - изменить заметку')
    print('6 - закрыть приложение')


def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Введите команду от 1 до 6: "))

        if user_choice == 1:
            show_notes(file_name)  #+- добавить выборку по дате, доп метод наверное
        elif user_choice == 2:
            add_note(file_name)   #+
        elif user_choice == 3:
            search_note(file_name)  #+
        elif user_choice == 4:
            delete_note(file_name)
        elif user_choice == 5:
            rename_note(file_name) #+ -добавить изменение заголовка
        elif user_choice == 6:
            print('До свидания!')
            return


main('notes.csv')
