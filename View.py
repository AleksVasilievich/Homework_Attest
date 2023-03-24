class View:
    def view_id(self):
        a = ''
        array = list()
        array1 = list()
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array[0]:
                for j in i:
                    if j != ';':
                        a += j
                    elif j == ';':
                        break
                array1.append(a)
                a = ''
            print(array1)
            return array1
