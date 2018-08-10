from flask import request
import requests as rt
import docker
import yaml
import re
from controllers.pipeline.controller import pipelineCtrl
from controllers.build.controller import buildCtrl
from application.appx import app
from flask_cors import CORS

CORS(app)
app.register_blueprint(pipelineCtrl, url_prefix='/pipeline')
app.register_blueprint(buildCtrl, url_prefix="/build")

client = docker.from_env()

@app.route("/")
def hello():
    print('hello')
    # return app.send_static_file('../web/dist/index.html')
    return "hello"

# def exe(task):
#     result = client.containers.run(task['image'], task['command'], detach=False, stdout=True, stderr=True).decode("utf-8")
#     print (result)
#     return result

# def configHandler(data):
#     print('data', data)
#     tasks = data['tasks']
#     result = {}
#     for taskName in tasks:
#         task = tasks[taskName]
#         result[taskName] = exe(task)
#     return str(result)

# @app.route("/execute", methods=['POST'])
# def execute():
#     git_url = request.form['git_url']}
#     print("execute url", git_url)
#     build_file_url = re.sub("github.com", "raw.githubusercontent.com", git_url)
#     build_file_url = re.sub(".git$", "/master/build.yml", build_file_url)
#     print(build_file_url)
#     build_file = rt.get(build_file_url).text
#     print(build_file)
#     data = yaml.load(build_file)
#     return configHandler(data)

# atexit.register(closeCbChannel)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
