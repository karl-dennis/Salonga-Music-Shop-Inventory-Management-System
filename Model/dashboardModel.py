import sqlite3
class dashboardModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.create_database()

    def create_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def get_loa(self, emp_id):
        try:
            self.cursor.execute('''SELECT level_of_access FROM employees WHERE employee_id = ?''', (emp_id,))
            result = self.cursor.fetchone()
            if result:
                # print('In Model:', result[0])
                return result[0]
            else:
                print('No access level found for employee_id:', emp_id)
                return None
        except sqlite3.Error as e:
            print('Error in dashboard Model:', e)
            return None

    def get_username(self, emp_id):
        try:
            self.cursor.execute('''SELECT username FROM accounts WHERE employee_id = ?''', (emp_id,))
            result = self.cursor.fetchone()
            if result:
                # print('In Model:', result[0])
                return result[0]
            else:
                print('no username found for employee_id:', emp_id)
                return None
        except sqlite3.Error as e:
            print('Error: ',e)