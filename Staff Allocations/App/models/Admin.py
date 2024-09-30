from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Admin(db.Model):
    AdminID = db.Column(db.Integer, primary_key=True)
    AdminName = db.Column(db.String(50),nullable=False)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, admin_name,username, password):
        self.AdminName = admin_name
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'AdminID': self.AdminID,
            'AdminName': self.AdminName,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)