from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    model = 'Lada Samara'
    issue = None
    solution_parts = []
    data = []

    for paragraph in doc.paragraphs:
        if paragraph.text.startswith('Вопрос'):
            # Сохраняем предыдущее решение, если оно существует
            if issue and solution_parts:
                solution = '\n'.join(solution_parts)
                data.append((model, issue, solution))
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
        data.append((model, issue, solution))

    return data

if __name__ == '__main__':
    data = read_docx('VAZ_2113i_14i_15i_Tretii_Rim.docx')
    for record in data:
        print(f"Issue: {record[1]}\nSolution: {record[2]}\n")
