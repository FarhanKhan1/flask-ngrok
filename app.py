# from flask import Flask
# from flask_restful import Resource, Api
# from flask_ngrok import run_with_ngrok
# app = Flask(__name__)
# api = Api(app)
# run_with_ngrok(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run()


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