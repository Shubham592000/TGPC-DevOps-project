from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to DevOps CI/CD Project 🚀</h1>
    <h2>This is Experiment 3 using GitHub Actions!</h2>
    <p>Deployed using GitHub Actions</p>
    <p>Status: Application is running successfully ✅</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
