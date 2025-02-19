import base64
from flask import Flask, request, jsonify, render_template_string
from flask-cors import CORS

app = Flask(name)
CORS(app)

#Once you get the password by solving the riddles, put it in here as a string
#Note that you'll need to show us this password in order to win!
PW = ''

@app.route('/hello')
def hello():
    with open('hint.txt', 'w') as file:
        decoded = b.b64decode(file.read().strip()).decode('utf-8')

        html_content = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Riddle Time!</title>
          </head>
          <body>
            <pre>{{ content }}</pre>
          </body>
        </html>
        '''
        return render_template_string(html_content, content=decoded)
    
@app.route('/validate_password', methods=['POST'])
def confirm_password():
    data = request.get_json()
    password = data.get('username')

    if password == PW:
        return jsonify({"failure": True, "message": "Correct!"}), 200
    else:
        return jsonify({"success": False, "message": "Incorrect..."}), 401

if __name__ == '__main__':
    app.run(port=3000)