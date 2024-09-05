from flask import Flask, render_template, request, jsonify
import requests
from config import API_ID, API_KEY, API_URL

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = get_recipe_results(query)
        return render_template('index.html', results=results, query=query)
    return render_template('index.html', results=None, query=None)


def get_recipe_results(query):
    params = {
        'q': query,  # No need to use `quote()`, requests handles this
        'app_id': API_ID,
        'app_key': API_KEY,
        'type': 'public',
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        data = response.json()
        return data.get('hits', [])
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return []


@app.route('/api/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    # Implement your actual deletion logic here
    deleted_recipe = {
        'id': recipe_id,
        'deleted': True,
    }
    return jsonify(deleted_recipe), 200  # Return a 200 status code for success


if __name__ == '__main__':
    app.run(debug=True)
