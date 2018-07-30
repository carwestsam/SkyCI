from datetime import datetime
from flask import Blueprint
from sqlalchemy.sql.expression import func
from application.appx import db
from models.Build import Build
import uuid
import requests as rqt
import re
import yaml

main = Blueprint('main', __name__)


@main.route('/')
def index():
	return "Main"

def trigger_build(pipeline):

	build_file_url = re.sub("github.com", "raw.githubusercontent.com", git_url)
	build_file_url = re.sub(".git$", "/master/build.yml", build_file_url)
	print(build_file_url)
	build_file = rqt.get(build_file_url).text
	previous_build = Build.query(id = pipeline.id).query(func.count(Build.id))

	build = Build(id=uuid.uuid4(),
				  pipeline_id=pipeline,
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
