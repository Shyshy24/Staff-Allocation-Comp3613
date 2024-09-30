from App.database import db

class Tutor(db.Model):
    TutorID = db.Coulmn(db.Integer,primary_key=True)
    TutorName = db.Coulmn(db.String(80),nullable=False)
    TutorRole = db.Coulmn(db.String(50),nullable=False)
    
    courses = db.relationship('Course', secondary='course_tutors', back_populates='tutors')
    
    def __intit__(self,TutorName,TutorRole):
        self.TutorName = TutorName
        self.TutorRole = TutorRole
    
    def get_json(self):
        return{
            'TutorID' : self.TutorID,
            'TutorName' : self.TutorName,
            'TutorRole' : self.TutorRole,
            'Courses' : [course.get_json() for course in self.courses]
        }
        
courses_tutors = db.Table('course_tutor',
        db.Coulmn('CourseID',db.Integer.db.ForgeinKey('course.CourseID')),
        db.Coulmn('TutorID',db.Integer,db.ForiegnKey('Tutor.TutorID'))
        )