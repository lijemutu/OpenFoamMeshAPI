
def template_for(tutorial_name):
    with open(tutorial_name,'r',encoding='utf-8') as openfile:
        return openfile.read()