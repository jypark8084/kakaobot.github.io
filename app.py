from flask import Flask, jsonify, request

app = Flask(__name__)

# 숫자 초기값 설정
number = 0

@app.route('/get_number', methods=['GET'])
def get_number():
    return jsonify({'number': number})

@app.route('/update_number', methods=['POST'])
def update_number():
    global number
    data = request.get_json()
    
    if data['operation'] == 'add':
        number += data['value']
    elif data['operation'] == 'subtract':
        number -= data['value']

    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True)
