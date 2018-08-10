from models.Task import Task
import uuid
import json
from application.appx import db
import pika


def dispatchTasks(tasksConfigs, build_id):
    # print(tasksConfigs)
    rawTasks = []
    for taskName in tasksConfigs['tasks']:
        task = tasksConfigs['tasks'][taskName]
        task['returnChannel'] = 'default'
        rawTasks.append(task)
    
    tasks = []
    
    for rawtask in rawTasks:
        task = Task(
                    id = uuid.uuid4(),
                    next = None,
                    build_id = build_id,
                    state = 'pending',
                    config_file = json.dumps(rawtask)
                )
        
        tasks.append(task)

    eofTask = Task(
            id = uuid.uuid4(),
            next = None,
            build_id = build_id,
            state = 'pending',
            config_file = json.dumps({
                'type': 'eof',
                'returnChannel': 'default'
            }))
    tasks.append(eofTask)

    for i in range(len(tasks)-1):
        print (i, tasks[i].id)
        tasks[i].next = str(tasks[i+1].id)
    
    for task in tasks:
        db.session.add(task)
        print(task)
    
    db.session.commit()

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='tasks')
    channel.basic_publish(exchange='',
                        routing_key='tasks',
                        body=json.dumps(tasks[0].toJSON()))

    connection.close()

    return tasks[0]

    
    
        
    
        
