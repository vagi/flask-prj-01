from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask object
app = Flask(__name__)

# Initialize Fernet object for encryption/decryption
key = Fernet.generate_key()
f = Fernet(key)

# A decorator used to tell the application that root page
# to be loaded
@app.route('/')
def get_main():
    return render_template('index_args.html')


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/encrypt')
def get_text():
    """
    Get parameter string (str) from URL query string and
    pass it to Fernet encryption method.
    Returns:
        HTML page to be loaded and token (bytes str)
    """

    # Getting input of text in URL's query string
    # Once empty input sent the default "Hello World!" is used
    string = request.args.get(
        'string',
        "Hello World!",
    )
    # Converting the text into bytes type
    text_to_bytes = string.encode('utf-8')
    # Encrypting the text
    token = f.encrypt(text_to_bytes)
    # Removing prefix "b" with single quotes
    token_ = token.decode()
    return render_template('index_args.html', operation='Encrypted', token=token_)


# A decorator used to tell the application which URL is
# associated with the following function
@app.route('/decrypt')
def get_token():
    """
    Get parameter string (str) from URL query string and
    pass it to Fernet decryption method.
    Returns:
        HTML page to be loaded and decrypted token in form of
        plain text (str)
    """

    # Getting input of token in URL's query string
    token = request.args.get(
        'string',
        "You didn't enter your token",
    )
    # Converting the string into bytes type
    token_to_bytes = token.encode('utf-8')
    # Decrypting the token into text
    output = f.decrypt(token_to_bytes)
    # Removing prefix "b" with single quotes
    output_ = output.decode()
    return render_template('index_args.html', operation='Decrypted', token=output_)


# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
