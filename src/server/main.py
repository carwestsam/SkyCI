from flask import Flask, Response, request
import docker
import yaml
import os

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
    result = str(client.containers.run(task['image'], task['command'], detach=False, stdout=True, stderr=True)) + '\n'
    print (result)
    return result

@app.route("/execute", methods=['POST'])
def execute():
    image = request.form['image_name']
    command = request.form['build_script']
    print("execute")
    task = {"image": image, "command": command}
    return exe(task)

@app.route("/hello")
def helloFromDocker():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/skyci.yml', 'r')
    server = yaml.load(f.read())
    print(config)
    tasks = config['tasks'] 

    return Response(generate())

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=9001)
