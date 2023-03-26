from Read import Read
from Input_notes import Input_notes
from Save import Save
from View import View
from Read_id import Read_id
from Delete import Delete
from Exit import Exit
from Edit import Edit
from Deletes import Deletes
class Menu:

    def menu(self):
        dls = Deletes()
        ed = Edit()
        ex = Exit()
        dl = Delete()
        rd = Read_id()
        vi = View()
        se = Save()
        re = Read()
        print("Программа - Заметки")
        print(
            "Введите ___ 1 - создать ; 2 - читать ; 3 - читать по ID; 4 - редоктировать ; 5 - удалить всё ; 6 - Удалить по ID ; 7 -  выход")
        comand = input()

        if comand == '1':
            se.save_notes(self), self.menu()
        elif comand == '2':
            re.reads_notes(), self.menu()
        elif comand == '3':
            rd.read_id_notes(), self.menu()
        elif comand == '4':
            ed.edit()
        elif comand == '5':
            dls.deletes()
        elif comand == '6':
            dl.delete_notes(), self.menu()
        elif comand == '7':
            ex.exit_notes()
        else:
            print("Error else")
        return comand