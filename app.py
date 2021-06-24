# Import required libraries
from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask object
app = Flask(__name__)

# Initialize Fernet object for encryption/decryption
key = Fernet.generate_key()
f = Fernet(key)


# Build tracking of page the user chosen and show a content of the page
@app.route('/')
@app.route('/index')
def get_index():
    params ={
        'operation_1': 'encryption',
        'operation_2': 'decryption',
    }
    return render_template(
        'index.html',
        **params
    )

# First method using args in url
#@app.route('/encrypt')
#def get_operation():
#    string = request.args.get(
#        'string', "You didn't enter your operation"
#    )
#    token = f.encrypt(b"string")
#    return f'Encrypted result: {token}'


# Second method using the Form
@app.route('/encrypt', methods=('GET', 'POST'))
def encryption():
    if request.method == 'GET':
        return render_template('form.html',)
    else:
        text = request.form["text"]
        token = f.encrypt(b'text')
        #return f'Encrypted result: {token}'
        return f"<i>Encrypted result:</i> <h3>{token}</h3>"


@app.route('/decrypt', methods=('GET', 'POST'))
def decryption():
    if request.method == 'GET':
        return render_template('form.html',)
    else:
        token_: bytes = b'request.form["text"]'
        output = f.decrypt(token_)
        #return f'Encrypted result: {output}'
        return f'<i>Decrypted result:</i> <h3>{output.decode()}</h3>'



# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
