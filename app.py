from flask import Flask, send_file

app = Flask(__name__)

TYPES = [
    'dttv',
    'tvlt',
    'cst',
    'bestPlayers'
]

@app.route('/')
@app.route('/home')
def welcome_page():
    return send_file('index.html')

@app.route('/html/<type_name>')
def chess_bot_type(type_name):
    if type_name in TYPES:
        return send_file(f'html/{type_name}.html')
    else:
        return "Loại không hợp lệ", 404

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
