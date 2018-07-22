from flask import Flask, Response, request
import requests as rt
import docker
import yaml
import os
import re

cwd = os.getcwd()
static_path = os.path.realpath(os.path.join(cwd , '../web'))
print('static_path', static_path)
if __name__ == "__main__":
    app = Flask(__name__, static_url_path='', static_folder=static_path)
else:
    app = Flask(__name__)

client = docker.from_env()

@app.route("/")
def hello():
    return app.send_static_file('index.html')

def exe(task):
    result = client.containers.run(task['image'], task['command'], detach=False, stdout=True, stderr=True).decode("utf-8")
    print (result)
    return result

def configHandler(data):
    print('data', data)
    tasks = data['tasks']
    result = {}
    for taskName in tasks:
        task = tasks[taskName]
        result[taskName] = exe(task)
    return str(result)

@app.route("/execute", methods=['POST'])
def execute():
    git_url = request.form['git_url']
    print("execute url", git_url)
    build_file_url = re.sub("github.com", "raw.githubusercontent.com", git_url)
    build_file_url = re.sub(".git$", "/master/build.yml", build_file_url)
    print(build_file_url)
    build_file = rt.get(build_file_url).text
    print(build_file)
    data = yaml.load(build_file)
    return configHandler(data)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9001)
