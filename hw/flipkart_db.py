import sqlite3

class DbModel:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mobiles (
                id INTEGER PRIMARY KEY,
                model TEXT,
                price TEXT,
                rating TEXT,
                image TEXT,
                description TEXT,
                reviews TEXT,
                specifications TEXT
            )
        ''')
        self.conn.commit()

    def get_all_mobile_names(self):
        self.cursor.execute("SELECT model FROM mobiles")
        return self.cursor.fetchall()

    def get_mobile_detail(self, model):
        self.cursor.execute("SELECT * FROM mobiles WHERE model = ?", (model,))
        return self.cursor.fetchone()

    def close_db_connection(self):
        self.conn.close()
