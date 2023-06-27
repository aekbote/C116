# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Avani" 
    age = "14"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Website")

def second_class():

    name = "Webs"
    return render_template("index.html", indexVariable = name)


# define the route to mother webpage
def second_class():

    name = "Mother"
    return render_template("index.html", indexVariable = name)


# define the route to friends webpage
def second_class():

    name = "Friends"
    return render_template("index.html", indexVariable = name)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
