from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {
        'movie' : 'Mr  and Mrs Smith',
        'actors' : [ 'Brad Pitt', 'Angelina Jolie'],
        'runtime' : int(127)
    }
]
@app.route('/')
def get_movies():
    return jsonify({'movies' : movies})

#app.run(port=5000)
