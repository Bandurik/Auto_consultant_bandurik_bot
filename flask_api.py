from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример заранее заданных ответов
predefined_answers = {
    "не заводится": "Проверьте аккумулятор и стартер.",
    "стук в двигателе": "Проверьте уровень масла и состояние поршней.",
    # Добавьте больше запросов и ответов по мере необходимости
}

@app.route('/generate_answer', methods=['POST'])
def generate_answer():
    data = request.json
    query = data.get('query')
    # Генерация ответа на основе заранее заданных данных
    answer = predefined_answers.get(query, "Извините, я не смог найти решение для вашей проблемы.")
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(port=5000)
