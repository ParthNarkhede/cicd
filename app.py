from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask app deployed using GitHub Actions and Kubernetes! Very Welcome from first deployment"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


