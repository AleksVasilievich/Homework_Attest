from  Error_notes import Error_notes
class Read:

    def reads_notes(self):
        er = Error_notes()
        try:
            with open('data.csv', 'r', encoding='utf_8') as file:
                return print(file.read())
        except Exception:
            print('er')
            er.error_notes()