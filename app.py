from flask import Flask
from flask_ngrok import run_with_ngrok
import webbrowser
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
