from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    
    <body>
    
    <form method = "post">
    <div>
        <label for ="rot">Rotate by: </label>
        <input type ="text" name = "rot" value ="0">
        <p class = "error"></p>
    </div>
    <textarea type = "text" name ="text"></textarea>
    <br>
    <input type = "submit">
    </form>    
    
    </body>
</html>
"""

@app.route("/", methods = ['POST'])
def encrypt():
    text2="text"
    rot2="rot" 
    output=rotate_string(text2, rot2)
    return render_template(output)


@app.route("/")
def index():
    return form

app.run()

