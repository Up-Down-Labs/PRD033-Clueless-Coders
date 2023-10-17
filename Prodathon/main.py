#impoting all the required libraries
from flask import Flask, redirect, render_template, request, url_for, flash



#creates an instance of flask application
app = Flask(__name__)

f = open('recipe.txt','a+')

def multidict_to_dict(recipe):
    dict={}
    for key, value in recipe.items():
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] = value
    return dict

def save_txt(new_recipe):
    for key, value in new_recipe.items():
            f.write('%s:%s\n' % (key, value))
            print('%s:%s\n' % (key, value))
            f.flush()

#Upload page

@app.route('/')
def upload():
    return render_template('upload.html')

#Browse page

@app.route('/browse', methods=['GET','POST'])
def browse():
    if request.method == 'POST':
        recipe = request.form
        new_recipe = multidict_to_dict(recipe)
        save_txt(new_recipe)
    return render_template('browse.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)