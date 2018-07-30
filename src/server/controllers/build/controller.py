from datetime import datetime
from flask import Blueprint
from sqlalchemy.sql.expression import func
from application.appx import db
from models.Build import Build
import uuid
import requests as rqt
import re
import yaml
from controllers.utils import *

buildCtrl = Blueprint('build', __name__)

@buildCtrl.route('/')
def index():
	return "Build"

@buildCtrl.route('/<pipeline_id>', methods=["GET"])
def listBuilds(pipeline_id="invalid"):
	builds = Build.query.filter_by(pipeline_id = pipeline_id).all()
	result = [o.toJSON() for o in builds]
	return jsr(result, 200)

def trigger_build(pipeline):
	build_file_url = re.sub("github.com", "raw.githubusercontent.com", pipeline.gitUrl)
	build_file_url = re.sub(".git$", "/master" + pipeline.ciCfgPath, build_file_url)
	print(build_file_url)
	build_file = rqt.get(build_file_url).text
	previous_build = db.session.query(func.count(Build.id)).filter(Build.pipeline_id == pipeline.id).scalar()
	print('***previous build***', previous_build)

	build = Build(id=uuid.uuid4(),
				  pipeline_id=pipeline.id,
				  type='default',
				  state='pending',
				  config_file=build_file,
				  build_index=previous_build + 1,
				  updateDatetime=datetime.utcnow())

	db.session.add(build)
	db.session.commit()

	print(build_file)
	data = yaml.load(build_file)

	return build

def bind_pipeline_config(build, pipeline):
	return None
