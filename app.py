# Import required libraries
from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask object
app = Flask(__name__)

# Initialize Fernet object for encryption/decryption operations
key = Fernet.generate_key()
f = Fernet(key)


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
@app.route('/encrypt', methods=('GET', 'POST'))
def encryption():
    if request.method == 'GET':
        return render_template('index.html',)
    else:
        # Getting input of text into the form
        user_input = request.form.get('text', 'Input your text')
        print("text:", user_input)
        # Converting the text into bytes type
        text_to_bytes = user_input.encode('utf-8')
        # Encrypting the text
        token = f.encrypt(text_to_bytes)
        return f"<i>Encrypted result:</i> <h3>{token}</h3>"

# A decorator used to tell the application which URL is
# associated with the following function
@app.route('/decrypt', methods=('GET', 'POST'))
def decryption():
    if request.method == 'GET':
        return render_template('index.html',)
    else:
        # Getting input of token into the form
        token_ = request.form['text']
        # Converting the string into bytes type
        token_to_bytes = token_.encode('utf-8')
        # Decrypting the token into text
        output = f.decrypt(token_to_bytes)
        return f'<i>Decrypted result:</i> <h3>{output.decode()}</h3>'


# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
