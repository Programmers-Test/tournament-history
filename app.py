from flask import Flask, send_file

app = Flask(__name__)

TYPES = [
    'dttv',
    'tvlt',
    'tkcg',
    'bestPlayers'
]

@app.route('/')
@app.route('/home')
def welcome_page():
    return send_file('index.html')

@app.route('/<type_name>')
def top(type_name):
    if type_name in TYPES:
        return send_file(f'top/{type_name}.html')
    else:
        return "Loại không hợp lệ", 404

@app.route('/<type_name>')
def leaderboard(type_name):
    if type_name in TYPES:
        return send_file(f'leaderboard/{type_name}.html')
    else:
        return "Loại không hợp lệ", 404

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
