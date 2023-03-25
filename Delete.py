from Notes import Notes
from Read_id import Read_id
from Read import Read
from Error_notes import Error_notes


class Delete:

    def delete_notes(self):
        er = Error_notes()
        rd = Read_id()
        try:
            l_notes = input('Удалить весь список нажмите - 1 , по ID - 2 ->   ')
            if l_notes == '1':
                with open('data.csv', 'w', encoding='utf_8') as file:
                    file.write('')
                    print('Ваши данные успешно удалены !!!')
            elif l_notes == '2':
                array1 = rd.read_id_notes()[0]
                print('Подтвердите свой выбор !!!')
                temp_array = rd.read_id_notes()[1]
                # print(array1), print(temp_array)
                array = array1[0:temp_array] + array1[(temp_array + 1):]
                with open('data.csv', 'w', encoding='utf_8') as file:
                    for i in array:
                        file.writelines('%s\n' % i)
                print('Эти данные удалены !!!')
        except Exception:
            er.error_notes()
