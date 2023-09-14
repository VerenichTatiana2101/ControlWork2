import os

from note_functions import add_note, delete_note, rename_note, search_note, search_note_date, show_notes

# список функций приложения
def drawing():
    print('1 - показать заметки')
    print('2 - добавить заметку')
    print('3 - найти заметку по заголовку')
    print('4 - найти заметки за определённую дату')
    print('5 - удалить заметку')
    print('6 - изменить заметку')
    print('7 - закрыть приложение')


def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        try:
            user_choice = int(input("Введите команду от 1 до 7: "))
        except ValueError:
            os.system('CLS')
            print('Некорректный ввод. Попробуйте еще раз.')
            input('нажмите любую клавишу')
            continue

        if user_choice == 1:
            show_notes(file_name) 
        elif user_choice == 2:
            add_note(file_name) 
        elif user_choice == 3:
            search_note(file_name) 
        elif user_choice == 4:
            search_note_date(file_name) 
        elif user_choice == 5:
            delete_note(file_name)  
        elif user_choice == 6:
            while True:
                draw()
                try:
                    choice = int(input('Введите 1 или 2: '))
                except ValueError:
                    os.system('CLS')
                    print('Некорректный ввод. Попробуйте еще раз.')
                    input('нажмите любую клавишу')
                    continue
                if choice == 1:
                    rename_note(file_name, 1) 
                    break
                if choice == 2:
                    rename_note(file_name, 2) 
                    break
                else:
                    os.system('CLS') 
                    print('Данные некорректны! ')
                    input('нажмите любую клавишу')
        elif user_choice == 7:
            print('До свидания!')
            return
        
def draw():
    print('1 - изменить заголовок')
    print('2 - изменить заметку')