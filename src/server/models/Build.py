from sqlalchemy.sql import func
from application.appx import db

from sqlalchemy.dialects.postgresql import UUID, TEXT

class Build(db.Model):
    __tablename__ = "build"

    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True)
    pipeline_id = db.Column(UUID(as_uuid=True))
    type = db.Column(db.String(120), unique=False, nullable=False)
    state = db.Column(db.String(120), unique=False, nullable=False)
    build_index = db.Column(db.BigInteger, nullable=False)
    config_file = db.Column(TEXT, nullable=False)
    createDatetime = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updateDatetime = db.Column(db.DateTime(timezone=True), nullable=False, onupdate=func.now())

    def __repr__(self):
        return '<Pipeline %r, url: %r>' % (self.name, self.gitUrl + self.ciCfgPath)

    def toJSON(self):
        return {
            "id": str(self.id),
            "pipelineId": str(self.pipeline_id),
            "state": self.state,
            "buildIndex": self.build_index,
            "configFile": self.config_file,
        }
