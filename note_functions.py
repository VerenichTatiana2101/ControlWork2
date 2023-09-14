import os
import uuid
import csv
from datetime import datetime

# показывает весь список по дате добавления
def show_notes(file_name):
    try:
        with open(file_name, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=';')
            count = 0

            for row in file_reader:
                if count == 0:
                    print(";".join(row))
                else:
                    print(row)
        with open(file_name, 'r') as file:
            data = file.readlines()
        input('\npress any key')
    except FileNotFoundError:
        print('Файл не найден')
        input('\npress any key')

# проверяет наличие файла, 
# при отсутствии создаёт с заголовками столбцов и добавляет заметку
# при наличии файла добавляет только новую заметку
def add_note(file_name):
    names = ["ID", " заголовок", " заметка", " дата"]
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(
            w_file, delimiter=';', lineterminator='\n', fieldnames=names)
        if not file_exists:
            file_writer.writeheader()
        title = input('Введите заголовок заметки: ').capitalize()
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


# ищет заметку по заголовку
def search_note(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        while True:
            title = input('Введите заголовок для поиска: ').capitalize()
            if title.strip():
                break
            else:
                os.system('CLS')
                print('Вы не ввели ничего. Попробуйте еще раз.')
       
        for row in reader:
            if title in row[1]:
                print(headers)
                print(row)
                break
        else:
            print('нет заметки с данным заголовком.')
    input('нажмите любую клавишу')


#показывает все заметки за дату введённую пользователем
def search_note_date(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        while True:
            date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
            try:
                date_time_obj = datetime.strptime(date_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                date = date_time_obj.date()   
            except ValueError:
                os.system('CLS')
                print('Неверный формат даты. Попробуйте еще раз.')
                continue
            notes_found = False
            for row in reader:
                row_date_time_obj = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                row_date = row_date_time_obj.date()
                if date == row_date:
                    if not notes_found:
                        print(headers)
                    print(row)
                    notes_found = True
            if not notes_found:
                print('нет заметок за эту дату.')
                break
            else: 
                break
    input('нажмите любую клавишу')


# изменение заметки в зависимости от выбора пользователя
# заголовка или тела заметки, 
# дата и время создания автоматически меняется на дату редактирования
def rename_note(file_name, param):
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        title = input('Введите заголовок заметки: ').capitalize()
        notes = []
        note_found = False
        for row in reader:
            if title in row[1]:
                new_body = input('Введите новые данные: ').capitalize()
                if not new_body.strip():
                    print('поле не может быть пустым!')
                else:
                    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    row[param] = new_body
                    row[3] = date
                    print('Заметка успешно изменена!')
                note_found = True
            notes.append(row)
        if not note_found:
            print('Заметка с данным заголовком не найдена.')
    with open(file_name, mode='w', newline='', encoding='utf-8') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(notes)
    input('Нажмите любую клавишу для продолжения работы')


# удаление заметки по заголовку
def delete_note(file_name):
    os.system('CLS')
    while True:
        title = input('Введите заголовок заметки: ').capitalize()
        if title.strip():
            break
        else:
            os.system('CLS')
            print('Заголовок не может быть пустым. Попробуйте еще раз.')
    found = False
    with open(file_name, mode='r', newline='', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        headers = next(reader)
        
        with open(file_name, mode='w', newline='', encoding='utf-8') as w_file:
            writer = csv.writer(w_file, delimiter=';')
            writer.writerow(headers)
            for note in reader:
                if title in note[1]:
                    found = True
                    print(f'Заметка "{note[1]}" удалена.')
                else:
                    writer.writerow(note)
            if not found:
                print('Нет заметки с таким заголовком.')
    input('нажмите любую клавишу')


