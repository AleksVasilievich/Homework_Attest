from Input_notes import Input_notes


class Save:

    def save_notes(self, notes):
        try:
            inp = Input_notes()
            notes = inp.input_notes()

            with open('data.csv', 'a', encoding='utf_8') as file:
                file.write(notes)
                print('Ваши данные успешно сохранены !!!')
                print(notes)
        except Exception:
            print("Создайте чтобы сохранить !!!")
