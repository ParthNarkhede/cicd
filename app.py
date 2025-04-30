from flask import Flask, render_template_string

app = Flask(__name__)

# Home route with button to redirect
@app.route('/')
def home():
    return render_template_string('''
        <h1>Hello from Flask app deployed using GitHub Actions and Kubernetes!</h1>
        <p>Very Welcome from first deployment, but new commit.</p>
        <p>Very Welcome from second deployment, but second commit and update</p>
        <form action="/about">
            <button type="submit">Go to About Page</button>
        </form>
    ''')

# About page
@app.route('/about')
def about():
    return render_template_string('''
        <h1>About Page</h1>
        <p>This is a second page from your Flask app! Now modified from the next commit.This is a chnage in file</p>
        <p>And this is the second commit from the second deployment</p>
        <a href="/">Back to Home</a>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
