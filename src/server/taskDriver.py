import atexit
import pika
from models.Task import Task
import json
from logs import log

cbConn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
cbChannel = cbConn.channel()
cbChannel.queue_declare(queue='default')

def callback(ch, method, properties, body):
    print("Front Received %r" % body)
    finished_task_id = body.decode('utf-8')
    finished_task = Task.query.filter_by(id=finished_task_id).first()
    print(finished_task.toJSON())

    next_task = Task.query.filter_by(id=finished_task.next).first()
    
    if next_task.next == None:
        print('build execute finished')
    else :
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='tasks')
        channel.basic_publish(exchange='',
                            routing_key='tasks',
                            body=json.dumps(next_task.toJSON()))
        connection.close()
        print('triggered', next_task.id)

cbChannel.basic_consume(callback,
                    queue='default',
                    no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def closeCbChannel():
    cbChannel.close()
    print('onExit')

atexit.register(closeCbChannel)

cbChannel.start_consuming()
