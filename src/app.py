
from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
        'hostname': (socket.gethostname()),
        'message': 'you are doing great, Mohan!',
        'deployed_by': 'ArgoCD',
        'deployed_on': 'Kubernetes',
        'env' : 'prod',
        'app_name' : 'pyth1'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'up'
    }),200


if __name__ == '__main__':

    app.run(host="0.0.0.0")
