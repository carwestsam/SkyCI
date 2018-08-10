import pika
import random
import json
import docker
from logs import log, dictLog

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

name = (random.random() * 100) // 2

print ('name', name)
channel.queue_declare(queue='tasks')

client = docker.from_env()

def callback(ch, method, properties, body):
    print(" [x] %d Received %r" % (name,body))
    task = json.loads(body)
    task_id = task['id']
    config_file = json.loads(task['config_file'])
    return_channel = config_file['returnChannel']
    print(" **** %r : %r **** " % (task_id, return_channel))

    container = client.containers.run(config_file['image'], config_file['command'], detach=True, stdout=False, stderr=False)
    result = container.wait()
    logs = container.logs()

    dictLog('info', {
        "task_id": task_id,
        "logs": logs,
        "error": result["Error"],
        "exitCode": result["StatusCode"]
    })

    print('container', result, logs)

    back = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    ch = back.channel()
    ch.queue_declare(queue=return_channel)

    ch.basic_publish(exchange='',
                        routing_key=return_channel,
                        body=task_id.encode('utf-8'))

    back.close()


channel.basic_consume(callback,
                      queue='tasks',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
