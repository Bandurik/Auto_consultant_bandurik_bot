import sqlite3

def create_db():
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    
    # Создание основной таблицы
    c.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        issue TEXT NOT NULL,
        solution TEXT NOT NULL
    )
    ''')
    
    # Создание виртуальной таблицы для полнотекстового поиска
    c.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS cars_fts USING fts5(model, issue, solution, content='cars', content_rowid='id')
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
