from Exit import Exit
from Input_notes import Input_notes
from Notes import Notes
from Read import Read


class Save(Input_notes):

    def save_notes(self, notes):
        try:
            inp = Input_notes()
            notes = inp.input_notes()
            re = Read
            ex = Exit()

            with open('data.csv', 'a', encoding='utf_8') as file:
                file.write(notes)
                print('Ваши данные успешно сохранены !!!')
                print(notes)
                # ex.exit_notes()
        except Exception:
            print("Создайте чтобы сохранить !!!")
