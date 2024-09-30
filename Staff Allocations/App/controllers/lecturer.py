from App.models import Lecturer, Course
from App.database import db

def add_lecturer(lecturer_id,lecturer_name,lecturer_role):
    new_lecturer= Lecturer(LecturerID=lecturer_id, LecturerName=lecturer_name,LecturerRole=lecturer_role)
    db.session.add(new_lecturer)
    db.session.commit()
    return lecturer_id

def update_lecturer(lecturer_id,lecturer_name=None,lecturer_role=None):
    lecturer = Lecturer.quer.get(lecturer_id)
    if lecturer:
        if lecturer_name:
            lecturer.LecturerName= lecturer_name
            if lecturer_role:
                lecturer.LecturerRole = lecturer_role
                db.session.add(lecturer)
                db.session.commit()
                return lecturer
        return None 
    
def assgin_lecturer(lecturer_id,course_id):
    lecturer = Lecturer.query.get(lecturer_id)
    course = Course.query.get(course_id)
    if lecturer and course:
        lecturer.courses.append(course)
        db.session.add(lecturer)
        db.session.commit()
        return lecturer
    return None

def delete_lecturer(lecturer_id):
    lecturer = Lecturer.query.get(lecturer_id)
    if lecturer:
        db.session.delete(lecturer)
        db.session.commit()
        return lecturer
    return None

def get_lecturer(lecturer_id):
    return Lecturer.query.get(lecturer_id)


def get_all_lecturers():
    return Lecturer.query.all()


def get_all_lecturers_json():
    lecturers = Lecturer.query.all()
    if not lecturers:
        return []
    return [lecturer.get_json() for lecturer in lecturers]


def get_lecturer_courses(lecturer_id):
    lecturer = Lecturer.query.get(lecturer_id)
    if lecturer:
        return lecturer.courses  
    return None
    
    