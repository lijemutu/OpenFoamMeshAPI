from flask import Flask
from tutorials import template_for
import os
app = Flask(__name__)

@app.route("/tutorials",methods =["GET"])
def template_box():
    return ' '.join(os.listdir("examples"))

@app.route("/tutorials/<name>",methods =["GET"])
def templates(name):
    return template_for("examples\\"+name)

if __name__ == '__main__':
    app.run()