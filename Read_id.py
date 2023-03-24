from View import View
from Error_notes import Error_notes


class Read_id:
    def read_id_notes(self):
        er = Error_notes()
        vi = View()
        try:
            arr = vi.view_id()
            temp = input(' Если УВЕРЕНЫ введите номер ID ->   ')
            temp_id = arr.index(temp)
            array = list()
            array1 = list()
            with open('data.csv', 'r', encoding='utf_8') as file:
                array.append(file.read().split())
                for i in array[0]:
                    array1.append(i)
            print(*array1[temp_id])
            return [array1, temp_id]
        except Exception:
            er.error_notes()