# from Menu import  Menu
from Input_notes import Input_notes
class Save:
    def save_notes(self, notes):
        print(5)
        # m = Menu()

        with open('data.csv', 'a', encoding='utf_8') as file:
            file.write(notes)
            print('Ваши данные успешно сохранены !!!'),
        # except Exception:
        #     print("Создайте чтобы сохранить !!!"), m.menu()
        # m.menu()