from application.appx import db
from sqlalchemy.dialects.postgresql import UUID, TEXT

class Task(db.Model):
	__tablename__ = 'task'

	id = db.Column(UUID(as_uuid=True), primary_key=True)
	next = db.Column(db.String(40))
	build_id = db.Column(db.String(40))
	state = db.Column(db.String(120), nullable=False)
	config_file = db.Column(TEXT, nullable=False)

