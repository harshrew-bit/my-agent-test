from flask import Flask, jsonify
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "uptime": time.time() - start_time})

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True)
