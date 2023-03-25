from Exit import Exit
from Input_notes import Input_notes
from Notes import Notes
from Read import Read

class Save(Input_notes):

    read_notes = ''

    def __init__(self):
        super().__init__()


    def get(self):
        return self.read_notes



    def save_notes(self):
        try:
            imp = Input_notes()
            read_notes = imp
            re = Read
            ex = Exit()
            print('Сохранить - 1 ; Выйти - 2 ; Меню - 3 ')
            temp = input()
            if temp == '1':
                with open('data.csv', 'a', encoding='utf_8') as file:
                    file.write(notes)
                    print('Ваши данные успешно сохранены !!!')
            elif temp == '2':
                ex.exit_notes()
            # elif temp == '3':
            #     re.reads_notes(self)

        except Exception:
            print("Создайте чтобы сохранить !!!")
