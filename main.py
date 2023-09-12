import os
from datetime import datetime

def show_notes(file_name):
    try:
        with open(file_name, 'r') as file: 
            data = file.readlines()
            if len(data) == 0:
                print('Файл пуст')
            else:
                for note in data:
                    if note.strip():
                        print(note, end='')
        input('\npress any key')
    except FileNotFoundError:
        print('Файл не найден')
        input('\npress any key')


def add_note(file_name):
    with open(file_name, 'a') as file:
        title = input('Введите заголовок заметки: ').title()
        body = input('Введите тело заметки: ')
        if not title.strip() or not body.strip():
            print('Заголовок или тело заметки не могут быть пустыми!')
        else:
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            file.write('\n' + title + ': ' + body + '; ' + date)
            print('Заметка успешно добавлена!')
    input('Нажмите любую клавишу для продолжения работы')


def search_note(file_name):
    os.system('CLS')
    target = input('Введите заголовок для поиска: ').title()

    with open(file_name, 'r') as file:
        notes = file.readlines()

        for note in notes:
            if target in note:
                print(note)
                break
        else:
            print('нет заметки с данным заголовком.')
    input('нажмите любую клавишу')


def delete_note(file_name):
    os.system('CLS')
    target = input('Ведите заголовок для удаления заметки: ').title()
    found = False

    with open(file_name, 'r') as file:
        notes = file.readlines()

    with open(file_name, 'w') as file:
        for note in notes:
            if target in note:
                print(note)
                found = True
                print('данные удалены')
            else:
                file.write(note)
        if not found:
            print('Нет заметки с таким заголовком.')
    input('нажмите любую клавишу')


def rename_note(file_name):
    os.system('CLS')
    target = input('Введите заголовок для поиска: ').title()

    with open(file_name, 'r') as file:
        notes = file.readlines()

    for i, note in enumerate(notes):
        if target in note:
            print(note)
            while True:
                rename_word = input('Введите данные для изменения: ').title()
                if ' ' not in rename_word:
                    break
                else:
                    print('Введите корректные данные! ')
            if rename_word in note:
                new_word = input('Введите сохраняемые данные: ').title()
                notes[i] = note.replace(rename_word, new_word)
                with open(file_name, 'w') as file:
                    file.writelines(notes)
            else:
                print('Данные не распознаны!')
            break
    else:
        print('нет заметки с данным именем.')
    input('нажмите любую клавишу')


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
            show_notes(file_name)
        elif user_choice == 2:
            add_note(file_name)
        elif user_choice == 3:
            search_note(file_name)
        elif user_choice == 4:
            delete_note(file_name)
        elif user_choice == 5:
            rename_note(file_name)
        elif user_choice == 6:
            print('До свидания!')
            return
    

main('notes.csv')