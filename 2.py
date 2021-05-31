from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("ku1")
    time.sleep(5)
    print("KU2")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(threaded=True)