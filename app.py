# Import required libraries
from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask object
app = Flask(__name__)


# Build tracking of page the user chosen and show a content of the page
@app.route('/')
def get_index():
    params ={
        'operation_1': 'encryption',
        'operation_2': 'decryption',
    }
    return render_template(
        'index.html',
        **params
    )


@app.route('/encrypt')
def get_operation():
    string = request.args.get(
        'string', "You didn't enter your operation"
    )
    return f'Operation: {string}'


@app.route('/encrypt/out', methods=('GET', 'POST'))
def transform():
    if request.method == 'GET':
        return '<form method="POST"> ' \
               '<input name="text"> ' \
               '<input type="submit"> ' \
               '</form>'
    else:
        text = request.form["text"]
        print(text)
        return f'Your text: {text}'


# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
