from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

opinions = []

@app.route('aronaworld.github.io/showerGeopo/')
def index():
    return render_template('index.html')

@app.route('/opinions', methods=['GET'])
def get_opinions():
    return jsonify(opinions)

@socketio.on('submit_opinion')
def handle_opinion(data):
    opinion = data['opinion']
    opinions.append(opinion)
    emit('new_opinion', opinion, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
