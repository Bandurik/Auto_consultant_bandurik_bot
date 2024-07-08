import openpyxl
from docx import Document

def import_from_docx_to_excel(docx_file, excel_file):
    doc = Document(docx_file)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Car Issues"

    ws.append(["Model", "Issue", "Solution"])  # Заголовки колонок
    model = 'Lada Samara'  # Укажем модель автомобиля, так как она едина для всех вопросов в документе
    issue = None
    solution_parts = []

    for paragraph in doc.paragraphs:
        if paragraph.text.startswith('Вопрос'):
            if issue and solution_parts:
                solution = '\n'.join(solution_parts)
                ws.append([model, issue, solution])
            try:
                issue = paragraph.text.split(': ')[1]
                solution_parts = []
            except IndexError:
                issue = None
        elif paragraph.text.strip():
            if issue:
                solution_parts.append(paragraph.text)
    
    if issue and solution_parts:
        solution = '\n'.join(solution_parts)
        ws.append([model, issue, solution])
    
    wb.save(excel_file)

if __name__ == '__main__':
    import_from_docx_to_excel('VAZ_2107.docx', 'car_repair_vaz_seven.xlsx')
