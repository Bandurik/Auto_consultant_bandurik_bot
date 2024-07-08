import sqlite3
from docx import Document

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
    
    conn.commit()
    conn.close()

def add_car_issue(model, issue, solution):
    conn = sqlite3.connect('car_repair.db')
    c = conn.cursor()
    c.execute("INSERT INTO cars (model, issue, solution) VALUES (?, ?, ?)", (model, issue, solution))
    conn.commit()
    conn.close()

def import_from_docx(file_path):
    doc = Document(file_path)
    model = 'Lada Samara'  # Укажем модель автомобиля, так как она едина для всех вопросов в документе
    issue = None
    solution_parts = []

    for paragraph in doc.paragraphs:
        if paragraph.text.startswith('Вопрос'):
            # Сохраняем предыдущее решение, если оно существует
            if issue and solution_parts:
                solution = '\n'.join(solution_parts)
                add_car_issue(model, issue, solution)
            # Начинаем новый вопрос
            try:
                issue = paragraph.text.split(': ')[1]
                solution_parts = []
            except IndexError:
                issue = None
        elif paragraph.text.strip():  # Проверяем, что параграф не пустой
            if issue:
                solution_parts.append(paragraph.text)
    
    # Сохраняем последнее решение
    if issue and solution_parts:
        solution = '\n'.join(solution_parts)
        add_car_issue(model, issue, solution)

if __name__ == '__main__':
    create_db()
    import_from_docx('VAZ_2113i_14i_15i_Tretii_Rim.docx')
