from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    import os
    return "Hello World!%s"%os.environ

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
