from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify({
        'id': 1,
        'name': 'Saketh',
        'email': 'saketh@example.com'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

