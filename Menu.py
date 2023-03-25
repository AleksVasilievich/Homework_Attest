from Read import Read
from Input_notes import Input_notes
from Save import Save
from View import View
from Read_id import Read_id
from Delete import Delete
from Exit import Exit


class Menu:

    # def __init__(self, read_notes):
    #     Input_notes.__init__(self, read_notes)
    #
    #

    def menu(self):

        ex = Exit()
        dl = Delete()
        rd = Read_id()
        vi = View()
        se = Save()
        inp = Input_notes()
        inp1 = Input_notes()
        re = Read()
        print("Программа - Заметки")
        print(
            "Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - читать по ID; 5 - редоктировать ; 6 - удалить ; 7 - выход")
        comand = input()

        if comand == '1':
            inp.input_notes(), self.menu()
        elif comand == '2':
            # se.save_notes(inp1.input_notes())
            se.save_notes()
        elif comand == '3':
            print(3)
            re.reads_notes(), self.menu()
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
            ex.exit_notes()
        else:
            print("Error else")
        return comand

    # def show(self):
    #     return self.read_notes
