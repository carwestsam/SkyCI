from flask import Flask
import docker
app = Flask(__name__)
client = docker.from_env()

@app.route("/")
def hello():
    return "Hello Worlx from Flask"

@app.route("/hello")
def helloFromDocker():
    x = client.containers.run("ubuntu:16.04", "echo hello world", detach=False, stdout=True) 
    return x

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

# import docker

# client = docker.from_env()

# x = client.containers.run("ubuntu:16.04", "echo hello world", detach=False, stdout=True)

# print (str(x))  
