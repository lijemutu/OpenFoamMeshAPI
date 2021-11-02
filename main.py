from flask import Flask
from flask import request
from flask.wrappers import Response
from TemplateFromFile import TemplateFromFile
import os
from flask import make_response,jsonify
app = Flask(__name__)

@app.route("/",methods=["GET"])
def sanity():

    return "Ok"

@app.route("/tutorials",methods =["GET"])
def template_list():
    return make_response(jsonify(templates_available = sorted(os.listdir("examples"))),200)

@app.route("/tutorials/<string:name>",methods =["GET"])
def templates(name):

    if name not in os.listdir("examples"):
        return Response("Resource not found",status=404)

    template_name = TemplateFromFile("examples/"+name)

    if request.args.get('download') == '1':
        template_name.template_retrieve()
        return template_name.blockMeshDict
    return template_name.template_response(200)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)    