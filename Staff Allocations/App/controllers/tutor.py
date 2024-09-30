from App.models import Tutor, Course
from App.database import db

def add_tutor(tutor_id, tutor_name, tutor_role):
    new_tutor = Tutor(TutorID = tutor_id, TutorName= tutor_name, TutorRole=tutor_role)
    db.session.add(new_tutor)
    db.session.commit()
    return new_tutor

def update_tutor(tutor_id, tutor_name=None, tutor_role=None):
    tutor = Tutor.query.get(tutor_id)
    if tutor:
        if tutor_name:
            tutor.TutorName = tutor_name
        if tutor_role:
            tutor.TutorRole = tutor_role
        db.session.add(tutor)
        db.session.commit()
        return tutor
    return None

def delete_tutor(tutor_id):
    tutor = Tutor.query.get(tutor_id)
    if tutor:
        db.session.delete(tutor)
        db.session.commit()
        return tutor
    return None

def assgin_tutor(tutor_id,course_id):
    tutor = Tutor.query.get(tutor_id)
    course = Course.query.get(course_id)
    if tutor and course:
        tutor.courses.append(course)
        db.session.add(tutor)
        db.session.commit()
        return tutor
    return None
    
def get_tutor(tutor_id):
    return Tutor.query.get(tutor_id)


def get_all_tutors():
    return Tutor.query.all()


def get_all_tutors_json():
    tutors = Tutor.query.all()
    if not tutors:
        return []
    return [tutor.get_json() for tutor in tutors]


def get_tutor_courses(tutor_id):
    tutor = Tutor.query.get(tutor_id)
    if tutor:
        return tutor.courses  
    return None