import sqlite3

def check_database():
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cars")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    check_database()
