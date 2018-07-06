from flask import Flask, Response
import docker
import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + '/skyci.yml', 'r')
config = yaml.load(f.read())
print(config)

app = Flask(__name__)
client = docker.from_env()

@app.route("/")
def hello():
    return "Hello Worlx from Flask"

@app.route("/hello")
def helloFromDocker():
    tasks = config['tasks']
    def generate():
        for taskName in tasks:
            task = tasks[taskName]
            print (task)
            yield str(client.containers.run(task['image'], task['command'], detach=False, stdout=True)) + '\n'
    return Response(generate())

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8081)
