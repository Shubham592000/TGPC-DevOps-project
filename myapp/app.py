from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>DevOps CI/CD Pipeline 🚀</h1>
    <p>Deployed using GitHub Actions</p>
    <p>Status: Running ✅</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
