
from flask import Flask, request, jsonify
from utils.math_utils import add_numbers
from utils.string_utils import normalize_name

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json(silent=True) or {}
    nums = data.get('numbers', [])
    try:
        total = add_numbers(nums)
    except TypeError:
        return jsonify({'error': 'numbers must be numeric'}), 400
    return jsonify({'sum': total})

@app.route('/users', methods=['POST'])
def create_user():
    payload = request.get_json(silent=True) or {}
    name = payload.get('name', '')
    if not isinstance(name, str) or not name.strip():
        return jsonify({'error': 'name is required'}), 400
    return jsonify({'name': normalize_name(name)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
