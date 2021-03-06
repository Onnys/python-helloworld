from flask import Flask, jsonify
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status request successfull')
    return jsonify({
        "result": "OK - healthy"
    })

@app.route("/metrics")
def metrics():
    app.logger.info('Metrics request successfull')
    return jsonify({
        "data": "{UserCount: 140, UserCountActive: 23}"
    })

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='info.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
