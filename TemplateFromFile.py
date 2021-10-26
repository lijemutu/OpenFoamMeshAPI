from Template import Template
from flask import jsonify, make_response
class TemplateFromFile(Template):

    def template_retrieve(self):
        with open(self.templateName,'r',encoding='utf-8') as openfile:
            self.blockMeshDict = openfile.read()
            return self.blockMeshDict

    def template_response(self,statusCode:int):
        return make_response(jsonify(blockMeshDict = self.template_retrieve()),statusCode)