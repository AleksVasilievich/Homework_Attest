from datetime import datetime
from View import View
from Error_notes import Error_notes


class Input_notes:

    def input_notes(self):
        er = Error_notes()
        vi = View()

        array2 = vi.view_id()
        try:

            id_int = abs(int(input('Введите натуральное число, новый id ->  ')))
            for i in array2:
                while i == str(id_int):
                    print('id уже существует !!!')
                    id_int = abs(int(input('Введите натуральное число, новый id ->  ')))
            id_str = str(id_int)
            head_n = input('Введите заголовок ->  ')
            body_n = input('Введите текст заметки ->  ')
            date_n = str(datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))
            notes = (id_str + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
            global read_notes
            read_notes = notes
            print('СОХРАНИТЬ ДАННЫЕ ???-- НАЖМИТЕ --  2 -- ИЛИ ДАННЫЕ БУДУТ ПОТЕРЯНЫ !!!')
            temp = input()
            if temp == '2':
                return read_notes
            else:
                print('ДАННЫЕ НЕ СОХРАНЕНЫ  !!!')

        except Exception:
            er.error_notes()
