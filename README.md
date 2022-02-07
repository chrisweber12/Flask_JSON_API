# Flask JSON API

Simple Python-JSON API implemented with Flask

### Usage

The *bootstrap.sh* file will do all the work in running the API - it initializes the Flask app, sources to the virtual environment, and runs the app. In the main directory, simply run the command `./bootstrap.sh`.

From here, you can navigate to http://localhost:3000 and you will see a welcome page. At http://localhost:3000/recipes, you will see the names of the recipes contained in *data.json* in JSON format. Recipe details can be found at http://localhost:3000/recipes/details/{recipeName} (case sensitive).

Recipes can be added by issuing a POST request. One way to do this is by following the format of this example shell command:
```sh
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "<newRecipeName>",
  "ingredients": ["<ingredient1>", "<ingredient2>", "<ingredient3>"],
  "instructions":["<step1>", "<step2>"]
}' http://localhost:3000/recipes
```

Existing recipes can also be modified by issuing a PUT request. An example is shown similarly below:
```sh
curl -X PUT -H "Content-Type: application/json" -d '{
  "name": "<existingRecipeName>",
  "ingredients": [""<newIngredient1>", "<newIngredient2>", "<newIngredient3>"],
  "instructions":["<newStep1>", "<newStep2>"]   
}' http://localhost:3000/recipes
```
Added and modified recipes write to *data.json*, so any modifications will still be present after quitting the program and re-running it.
