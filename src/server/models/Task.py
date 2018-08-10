from application.appx import db
from sqlalchemy.dialects.postgresql import UUID, TEXT
from sqlalchemy.sql import func

class Task(db.Model):
	__tablename__ = 'task'

	id = db.Column(UUID(as_uuid=True), primary_key=True)
	next = db.Column(db.String(40))
	build_id = db.Column(db.String(40))
	state = db.Column(db.String(120), nullable=False)
	config_file = db.Column(TEXT, nullable=False)
	# createDatetime = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
	# updateDatetime = db.Column(db.DateTime(timezone=True), nullable=False, onupdate=func.now())

	def toJSON(self):
		return {
			'id': str(self.id),
			'next': self.next,
			'build_id': self.build_id,
			'state': self.state,
			'config_file': self.config_file
		}