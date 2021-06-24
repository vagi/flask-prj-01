# Import required libraries
from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask object
app = Flask(__name__)

# Initialize Fernet object for encryption/decryption
key = Fernet.generate_key()
f = Fernet(key)


# Build tracking of page the user chosen and show a content of the page
#@app.route('/')
#@app.route('/index')
#def get_index():
#    params ={
#        'operation_1': 'encryption',
#        'operation_2': 'decryption',
#    }
#    return render_template(
#        'index.html',
#        **params)

# First method using args in url
#@app.route('/encrypt')
#def get_operation():
#    string = request.args.get(
#        'string', "You didn't enter your operation"
#    )
#    token = f.encrypt(b"string")
#    return f'Encrypted result: {token}'


# Second method using the Form
@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
@app.route('/encrypt', methods=('GET', 'POST'))
def encryption():
    if request.method == 'GET':
        return render_template('index.html',)
    else:
        user_input = request.form["text"]
        text_to_bytes = user_input.encode('utf-8')
        token = f.encrypt(text_to_bytes)
        return f"<i>Encrypted result:</i> <h3>{token}</h3>"


@app.route('/decrypt', methods=('GET', 'POST'))
def decryption():
    if request.method == 'GET':
        return render_template('index.html',)
    else:
        token_ = request.form["text"]
        token_to_bytes = token_.encode('utf-8')
        output = f.decrypt(token_to_bytes)
        return f'<i>Decrypted result:</i> <h3>{output.decode()}</h3>'



# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
