import sqlite3

def add_car_issue(model, issue, solution):
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("INSERT INTO cars (model, issue, solution) VALUES (?, ?, ?)", (model, issue, solution))
    c.execute("INSERT INTO cars_fts (rowid, model, issue, solution) VALUES (last_insert_rowid(), ?, ?, ?)", (model, issue, solution))
    conn.commit()
    conn.close()


def delete_car_issue(issue):
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("DELETE FROM cars WHERE issue = ?", (issue,))
    conn.commit()
    conn.close()

def update_car_issue(issue, new_solution):
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("UPDATE cars SET solution = ? WHERE issue = ?", (new_solution, issue))
    conn.commit()
    conn.close()

def list_car_issues():
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cars")
    rows = c.fetchall()
    conn.close()
    return rows

def remove_duplicates():
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute('''
    DELETE FROM cars
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM cars
        GROUP BY model, issue, solution
    )
    ''')
    conn.commit()
    conn.close()
