from flask import Flask, Response
import docker
import yaml
import os

static_path = os.path.realpath(os.path.join(dir_path , '../web'))
print('static_path', static_path)
if __name__ == "__main__":
    app = Flask(__name__, static_url_path='', static_folder=static_path)
else:
    app = Flask(__name__)

client = docker.from_env()

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/hello")
def helloFromDocker():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/skyci.yml', 'r')
    server = yaml.load(f.read())
    print(config)
    tasks = config['tasks'] 
    def generate():
        for taskName in tasks:
            task = tasks[taskName]
            print (task)
            try:
                result = str(client.containers.run(task['image'], task['command'], detach=False, stdout=True, stderr=True)) + '\n'
                print (result)
            except docker.errors.ContainerError as error:
                print(error)
                result = str(error)
            except docker.errors.ImageNotFound as error:
                print(error)
                result = str(error)
            yield result
    return Response(generate())

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8081)
