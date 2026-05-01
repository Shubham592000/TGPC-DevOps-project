from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to DevOps CI/CD Project 🚀</h1>
    <h2>This is Experiment 4: Write a Docker file to containerize a Python Flask application.</h2>
    <p>Deployed using Docker container</p>
    <p>Status: Application is running successfully on container ✅</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
