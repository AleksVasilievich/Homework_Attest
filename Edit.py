import csv
from Input_notes import Input_notes
from Read import Read
from Read_id import Read_id
from View import View
from Save import Save
from Delete import Delete
class Edit:
    def edit(self):
        print('Удалим редактируемую заметку на новую ')
        de = Delete()
        de.delete_notes()
        se = Save()
        se.save_notes(self)
        # vi = View()
        # rd = Read_id()
        # re = Read()
        # arr = vi.view_id()







        # re.reads_notes()
        # temp_array = rd.read_id_notes()[1]

        # temp = input('ID для редоктирования ->   ')
        # temp_array = arr.index(temp)
        # array1 = rd.read_id_notes()[0]
        # print('Подтвердите свой выбор !!!')
        # # print(array1), print(temp_array)
        # array = array1[0:temp_array] + array1[(temp_array + 1):]
        # with open('data.csv', 'w', encoding='utf_8') as file:
        #     for i in array:
        #         file.writelines('%s\n' % i)
        #
        #
        # rd.read_id_notes()
        # # print(('ID для редоктирования ->   '))
        # # arr = vi.view_id()
        # inp = Input_notes()
        # print('Заметка будет заменена, используя старый текст создадим новую ')
        # # inp.input_notes()
        # se.save_notes(self)
        #


        # with open('data.csv', 'r') as file:
        #     file1 = list(csv.reader(file))
        # # file1[0] = ''
        # print(file1[0])


        #
        # with open('data.csv', 'r') as f:
        #     incl_col = [0, 1, 2, 3]
        #     data1 = []
        #     reader = csv.reader(f, delimiter=";")
        #     for row in reader:
        #         col = list(row[i] for i in incl_col)
        #         print(col)
        #         data1.append(col)
        #
        # with open('data1.csv', 'w') as f:
        #     writer = csv.writer(f, delimiter=";")
        #     writer.writerows(data1)
        #
        # return
