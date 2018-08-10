
from datetime import datetime
import pymongo
from pymongo import MongoClient
import urllib.parse


# client = MongoClient()
username = urllib.parse.quote_plus("root")
password = urllib.parse.quote_plus("example")
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password), 27017)

db = client['log-collection']
_logs = db.logs

def dictLog(level, dict_messsage):
    record = {
        "date": datetime.utcnow(),
        "level": level
    }
    record.update(dict_messsage)
    print ("dictLog", record)
    _logs.insert_one(record)

def log(level, message):
    time = str(datetime.now())
    print(time, level, message)
