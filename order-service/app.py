from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/order', methods=['GET'])
def get_order():
    return jsonify({
        'order_id': 101,
        'user_id': 1,
        'product': 'Wireless Mouse',
        'status': 'Shipped'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

