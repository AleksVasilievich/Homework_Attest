import csv

from Read import Read
from Read_id import Read_id
from View import View
class Edit:
    def edit(self):
        vi = View()
        rd = Read_id()
        re = Read()
        # re.reads_notes()
        # rd.read_id_notes()
        arr = vi.view_id()
        temp = input(' Введите номер ID ->   ')
        temp_id = arr.index(temp)
        array = list()
        array1 = list()
        array2 = list()
        print(temp_id)
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array[0]:
                array1.append(i)
        print(array1[temp_id])
        print("Редактировать Заголовок - 1 ; Текст заметки - 2 ")
        lst_notes = ''
        for i in array1[temp_id]:
            if i != ';':
                lst_notes = lst_notes + i
                if i == ';':
                    break
                break
            break

        lst_notes = lst_notes + ';' + '' + ';' + '' +';'



        print(lst_notes)





        # with open('data.csv', 'r') as f:
        #     incl_col = [1, 2]
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

        # return
