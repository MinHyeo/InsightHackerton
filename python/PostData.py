from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/submit_code', methods=['POST'])
def submit_code():
    try:
        # JSON 형식으로 데이터 받기
        data = request.get_json()

        # 문제 번호와 코드 추출
        problem_num = data.get('problemNum')
        code = data.get('code')

        # 여기서 문제 번호와 코드를 처리
        print(f"Received problem number: {problem_num}")
        print(f"Received code:\n{code}")

        # 결과 반환 (예: 코드 실행 결과)
        return jsonify({"status": "success", "problemNum": problem_num, "code": code}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)