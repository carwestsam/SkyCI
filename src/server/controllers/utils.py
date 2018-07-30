from flask import Response
import json

def jsr(content, status=200):
    resp = Response(json.dumps({'content':content, 'code':status}), status=200, mimetype='application/json')
    return resp