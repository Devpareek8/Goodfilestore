from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'AB_Botz'


if __name__ == "__main__":
    app.run()
