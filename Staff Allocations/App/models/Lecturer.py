from App.database import db

class Lecturer(db.Model):
    LecturerID = db.Coulumn(db.Integer, primary_key=True)
    LecturerName = db.Coulumn(db.String(50),nullable=False)
    LecturerRole = db.Coulumn(db.String(50), nullable=False)
    
    courses = db.relationship('Course', secondary='course_lecturers', back_populates='lecturers')
    
    def __init__(self,lecturer_name,lecturer_role):
        self.LecturerName = lecturer_name
        self.LecturerRole = lecturer_role
        
    def get_json(self):
        return{
            'LecturerID': self.LecturerID,
            'LecturerName' : self.LecturerName,
            'LecturerRole' : self.LecturerRole,
            'Courses' : [course.get_json() for course in self.courses]
        }  