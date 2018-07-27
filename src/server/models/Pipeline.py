import sys
from sqlalchemy.sql import func
# sys.path.append("..")
from application.appx import db

from sqlalchemy.dialects.postgresql import UUID

class Pipeline(db.Model):
    __tablename__ = "pipeline"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    type = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    gitUrl = db.Column(db.String(255), unique=False, nullable=False)
    ciCfgPath = db.Column(db.String(255), unique=False, nullable=False)
    createDatetime = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updateDatetime = db.Column(db.DateTime(timezone=True), nullable=False, onupdate=func.now())

    def __repr__(self):
        return '<Pipeline %r, url: %r>' % (self.name, self.gitUrl + self.ciCfgPath)

    def toJSON(self):
        return {
            "id": str(self.id),
            "type": self.type,
            "name": self.name,
            "status": self.status,
            "gitUrl": self.gitUrl,
        }
