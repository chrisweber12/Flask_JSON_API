from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

with open('data.json') as file:
    data = json.load(file)

def writeData():
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
        file.write('\n')

def recipeNames():
    return [recipe['name'] for recipe in data['recipes']]

@app.route('/')
def index():
    return 'Welcome to the recipe page'

@app.route('/recipes')
def get_recipes():
    return jsonify({'recipeNames': recipeNames()})

@app.route('/recipes', methods=['POST'])
def add_recipe():
    if request.get_json()['name'] in recipeNames():
        return jsonify({'error':'Recipe already exists'}), 400
    else:
        data['recipes'].append(request.get_json())
        writeData()
        return '', 201

@app.route('/recipes', methods=['PUT'])
def alter_recipe():
    if request.get_json()['name'] not in recipeNames():
        return jsonify({'error':'Recipe does not exist'}), 404
    else:
        for i, recipe in enumerate(data['recipes']):
            if recipe['name'] == request.get_json()['name']:
                data['recipes'][i] = request.get_json()
        writeData()
        return '', 204

@app.route('/recipes/details/<recipeName>')
def details(recipeName):
    for recipe in data['recipes']:
        if recipe['name'] == recipeName:
            return jsonify({'details':{'ingredients':recipe['ingredients'],'numSteps':len(recipe['instructions'])}})
    return jsonify({})
