from flask import Flask, jsonify, request, g
import time
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.before_request
def start_timer():
    g.start_time = time.time()

@app.after_request
def log_request(response):
    if hasattr(g, 'start_time'):
        duration = time.time() - g.start_time
        logger.info(f"{request.method} {request.path} - Status: {response.status_code} - Duration: {duration:.4f}s")
    return response

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True)
