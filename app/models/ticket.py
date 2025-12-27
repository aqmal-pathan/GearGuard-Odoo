from app import db

class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default="todo")  
    # todo | in_progress | done

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    technician_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Ticket {self.title}>"
