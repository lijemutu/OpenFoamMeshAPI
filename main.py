from flask import Flask
from flask.wrappers import Response
from werkzeug.exceptions import abort
from TemplateFromFile import TemplateFromFile
import os
from flask import make_response,jsonify
app = Flask(__name__)

@app.route("/tutorials",methods =["GET"])
def template_list():
    return make_response(jsonify(templates_available = os.listdir("examples")),200)

@app.route("/tutorials/<string:name>",methods =["GET"])
def templates(name):

    if name not in os.listdir("examples"):
        return Response("Resource not found",status=404)

    template_name = TemplateFromFile("examples\\"+name)
    return template_name.template_response(200)

if __name__ == '__main__':
    app.run()   