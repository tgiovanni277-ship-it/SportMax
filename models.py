from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ContactMessage(db.Model):
    __tablename__ = "contact_messages"
    __table_args__ = (
        db.Index("ix_contact_messages_correo", "correo"),
        db.Index("ix_contact_messages_created_at", "created_at"),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)


    def __repr__(self):
        return f"<ContactMessage {self.id} {self.correo}>"
