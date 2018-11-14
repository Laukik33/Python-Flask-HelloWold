from flask import Flask
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route("/")
def index():
    send_magic_packet('1C.3E.84.14.6A.30')

if __name__ =="__main__":
    app.run(debug=True)
