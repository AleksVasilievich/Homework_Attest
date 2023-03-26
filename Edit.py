from Save import Save
from Delete import Delete


class Edit:
    def edit(self):
        print('Удалим редактируемую заметку и напишем новую ')
        de = Delete()
        de.delete_notes()
        se = Save()
        se.save_notes(self)
