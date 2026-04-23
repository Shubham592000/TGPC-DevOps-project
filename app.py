from flask import Flask
app = Flask(name)

@app.route('/')
def home():
    return "Hello from GitLab CI!"

app.run(host='0.0.0.0', port=5000)