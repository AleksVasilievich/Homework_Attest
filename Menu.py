from  Read import Read
from Input_notes import Input_notes
from Save import Save
from View import  View
from Read_id import Read_id
from Delete import Delete
class Menu:
    def menu(self):
        dl = Delete()
        rd = Read_id()
        vi = View()
        se = Save()
        inp = Input_notes()
        inp1 = Input_notes()
        re = Read()
        print("Программа - Заметки")
        print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - читать по ID; 5 - редоктировать ; 6 - удалить ; 7 - выход")
        comand = input()


        if comand == '1':
            inp.input_notes()
        elif comand == '2':
            print(2)
            se.save_notes()
        elif comand == '3':
            print(3)
            re.reads_notes()
        elif comand == '4':
            print(4)
            rd.read_id_notes(), self.menu()
        elif comand == '5':
            print(5)
            vi.view_id()
            # edit_notes()
        elif comand == '6':
            print(6)
            dl.delete_notes()
        elif comand == '7':
            print(7)

                # exit_notes()
            # elif comand == '8':
            #     deletes_notes()
        else:
                # error_notes()
            print("Error else")
        return comand

            # error_notes()
