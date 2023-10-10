from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
    data = response.json()
    pokemon_list = data['results']
    return render_template('index.html', pokemon_list=pokemon_list)

if __name__ == '__main__':
    app.run(debug=True)
 