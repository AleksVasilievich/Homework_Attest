from Error_notes import Error_notes


class Deletes:
    def deletes(self):
        try:

            temp = input('Если уверены нажмите - 5 ')
            if temp == '5':
                with open('data.csv', 'w', encoding='utf_8') as file:
                    file.write('')
                print('Ваши данные успешно удалены !!!')
        except Exception:
            print('Error')
