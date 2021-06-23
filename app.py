# Import some required Flask libraries
from flask import Flask, render_template, request

# Initialize Flask object
app = Flask(__name__)

# Build tracking of page the user chosen and show a content of the page
@app.route('/')
def get_index():
    return "<h1>Hello! You are on the Main page.</h1>"


# Inserting condition in case this file was used as not main application,
# i.e imported as a module
if __name__ == '__main__':
    app.run(debug=True)
