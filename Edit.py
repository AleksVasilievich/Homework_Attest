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
        print(temp_id)
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array[0]:
                array1.append(i)
        print(array1[temp_id])
        print("Редактировать Заголовок - 1 ; Текст заметки - 2 ")
        # temp1 = input()
        # if temp1 == '1':

        # return
