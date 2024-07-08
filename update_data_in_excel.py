import openpyxl

def update_data_in_excel(file_path, model, issue, solution):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    ws.append([model, issue, solution])
    wb.save(file_path)

if __name__ == '__main__':
    # Пример использования: добавление новой записи
    model = 'Lada Samara'
    issue = 'новый вопрос'
    solution = 'новое решение'
    update_data_in_excel('car_repair.xlsx', model, issue, solution)
