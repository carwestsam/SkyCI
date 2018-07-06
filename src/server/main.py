from flask import Flask
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
    x = client.containers.run("ubuntu:16.04", config['bash'], detach=False, stdout=True) 
    return x

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8081)
