from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    print('This works, too')
    return "Hello World!"

if __name__ == "__main__":
    application.run()

