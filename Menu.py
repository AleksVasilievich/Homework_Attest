from Read import Read
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
            "\n1 - создать\n2 - читать\n3 - читать по ID\n4 - редоктировать\n5 - удалить всё\n6 - удалить по ID\n7 - выход\nВведите номер операции")
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
            print("Поверьте вводимые данные")
        return comand
