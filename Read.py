from Error_notes import Error_notes
from Notes import Notes


class Read(Notes):
    def __init__(self):
        super().__init__()

    def reads_notes(self):
        er = Error_notes()
        try:
            with open('data.csv', 'r', encoding='utf_8') as file:
                return print(file.read())
        except Exception:
            print('er')
            er.error_notes()
