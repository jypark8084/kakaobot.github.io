from flask import Flask, request, jsonify

app = Flask(__name__)

# 초기 숫자 값 설정
current_value = 0

# 현재 숫자 반환
@app.route('/get_number', methods=['GET'])
def get_number():
    return jsonify({"number": current_value})

# 숫자 변경 (더하거나 빼기)
@app.route('/update_number', methods=['POST'])
def update_number():
    global current_value
    data = request.json
    if "operation" in data and "value" in data:
        if data["operation"] == "add":
            current_value += data["value"]
        elif data["operation"] == "subtract":
            current_value -= data["value"]
    return jsonify({"number": current_value})

# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
