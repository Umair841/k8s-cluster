from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ' deployment ok k8s cluster '

app.run(host='0.0.0.0', port=5000)
