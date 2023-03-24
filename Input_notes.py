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
            # date_n = input('Введите дату ->  ')
            date_n = str(datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))
            notes = (id_str + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
            global read_notes
            read_notes = notes
            print(read_notes), print('СОХРАНИТЬ ДАННЫЕ ???-- НАЖМИТЕ --  2 -- ИЛИ ДАННЫЕ БУДУТ ПОТЕРЯНЫ !!!')
            return notes
        except Exception:
            er.error_notes()


#   def error_notes():
#       return print('No Comand !')
#
# # def exit_notes():
# #     return print('Goodbye !')
#
# # def delete_notes():
# #     try:
# #         l_notes = input('Удалить весь список нажмите - 1 , по ID - 2 ->   ')
# #         if l_notes == '1':
# #             with open('data.csv', 'w', encoding='utf_8') as file:
# #                 file.write('')
# #                 print('Ваши данные успешно сохранены !!!')
# #                 global read_notes
# #                 # read_notes = ''
# #         elif l_notes == '2':
# #             array1 = read_id_notes()[0]
# #             temp_array = read_id_notes()[1]
# #             # print(array1), print(temp_array)
# #             array = array1[0:temp_array] + array1[(temp_array + 1):]
# #             with open('data.csv', 'w', encoding='utf_8') as file:
# #                 for i in array:
# #                     file.writelines('%s\n' % i)
# #             print()
# #             reads_notes()
# #         else:
# #             error_notes(), menu()
# #     except Exception:
# #         error_notes()
