from App.database import db

class Course(db.Model):
    CourseID = db.Coulmn(db.Integer,primary_key=True)
    CourseName = db.Coulmn(db.String(100),nullable=False)
    CourseInfo = db.Coulmn(db.String(255))
    
    AdminID = db.Coulmn(db.Integer,db.ForeignKey('admin.AdminID'),nullable=False)
    admin = db.relationship('Admin',back_populates='courses')
    
    lecturers = db.relationship('Lecturer', secondary='course_lecturers',back_populates='courses')
    tutors = db.relationship('Tutor', secondary='course_tutor',back_populates='courses')
    
    def __intit__(self, CourseName, CourseInfo, AdminID):
        self.CourseName = CourseName
        self.CourseInfo = CourseInfo
        self.AdminID = AdminID
        
    def get_json(self):
       return {
            'CourseID' : self.CourseID,
            'CourseName': self.CourseName,
            'CourseInfo': self.CourseInfo,
            'AdminID': self.AdminID,
            'Lecturers': [lecturer.get_json() for lecturer in self.lecturers],
            'Tutors': [tutor.get_json() for tutor in self.tutors]
        }
    