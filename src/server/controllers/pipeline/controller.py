from flask import Blueprint, request, Response
from models.Pipeline import Pipeline
from application.appx import db
import uuid
from datetime import datetime
import json
from sqlalchemy.exc import IntegrityError

pipelineCtrl = Blueprint('pipeline', __name__)

def jsr(content, status=200):
    resp = Response(json.dumps({'content':content, 'code':status}), status=200, mimetype='application/json')
    return resp

@pipelineCtrl.route('/', methods=["GET"])
def index():
    pls = Pipeline.query.filter(Pipeline.status != 'deleted').all()
    result = [o.toJSON() for o in pls]
    return jsr(result)

@pipelineCtrl.route('/', methods=["POST"])
def post():
    _pl = request.get_json()

    pl = Pipeline(id=uuid.uuid4(),
                  type=_pl['type'],
                  name=_pl['name'],
                  status='normal',
                  gitUrl=_pl['gitUrl'],
                  ciCfgPath=_pl['ciCfgPath'],
                  updateDatetime=datetime.utcnow())

    db.session.add(pl)
    try:
        db.session.commit()

        return jsr(pl.toJSON(), 201)

    except IntegrityError as e:
        print ("Integrity Error")
    finally:
        print ("down")

    return "Some Thing Wrong"

@pipelineCtrl.route('/pl/<pipeline_id>', methods=["DELETE"])
def delete(pipeline_id="invalid"):
    pl = Pipeline.query.filter_by(id=pipeline_id).first()

    if pl.status == 'deleted':
        return jsr({'message': 'pipeline already deleted'}, 410)

    pl.status = 'deleted'
    db.session.add(pl)
    try:
        db.session.commit()
    finally:
        print ('wrong at delete')

    print('delete pipeline ', pipeline_id)
    return "delete " + str(pipeline_id)

@pipelineCtrl.route('/pl/<pipeline_id>', methods=["GET"])
def get_pipeline(pipeline_id="invalid"):

    pl = Pipeline.query.filter_by(id=pipeline_id).first()
    if pl == None:
        return jsr({'error': 'Could not find this pipeline'}, 404)
    elif pl.status == 'deleted':
        return jsr({'error': 'pipeline already deleted'}, 404)
    else:
        return jsr(pl.toJSON(), 200)

@pipelineCtrl.route('/pl/<pipeline_id>', methods=["POST"])
def alter_pipeline(pipeline_id="invalid"):
    pl = Pipeline.query.filter_by(id=pipeline_id).first()
    if pl == None:
        return jsr({'error': 'Could not find this pipeline'}, 404)
    elif pl.status == 'deleted':
        return jsr({'error': 'pipeline already deleted'}, 404)
    else:
        npl = request.get_json()
        pl.type = npl['type']
        pl.name = npl['name']
        pl.gitUrl = npl['gitUrl']
        pl.ciCfgPath = npl['ciCfgPath']
        db.session.add(pl)
        db.session.commit()
        return jsr({'message':'update successfully',
                    'pipeline': pl.toJSON()}, 200)
