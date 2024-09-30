from App.database import Course, Lecturer, Tutor
from App.database import db 

def add_course(course_id, course_name,course_info,admin_id):
    new_course = Course(CourseID= course_id,CourseName=course_name,CourseInfo=course_info,AdminID=admin_id)
    db.session.add(new_course)
    db.session.commit()
    return new_course

def update_course(course_id,course_name=None,course_info=None):
    course= Course.query.get(course_id)
    if course:
        course.CourseName= course_name
    if course_info:
        course.CourseInfo = course_info
        db.session.add(course)
        db.session.commit()
        return course
    
def delete_course(course_id):
    course=Course.query.get(course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
    return None

def assign_lecturer(course_id,lecturer_id):
    course = Course.query.get(course_id)
    lecturer = Lecturer.query.get(lecturer_id)
    if course and lecturer:
        course.lecturers.append(lecturer)
        db.session.add(course)
        db.session.commit()
        return course 
    return None

def assign_tutor(course_id,tutor_id):
    course = Course.query.get(course_id)
    tutor = Tutor.query.get(tutor_id)
    if course and tutor:
        course.tutor.append(tutor)
        db.session.add(course)
        db.session.commit()
        return course
    return None

def get_course(course_id):
    return Course.query.get(course_id)


def get_all_courses():
    return Course.query.all()


def get_all_courses_json():
    courses = Course.query.all()
    if not courses:
        return []
    return [course.get_json() for course in courses]


def get_course_lecturers(course_id):
    course = Course.query.get(course_id)
    if course:
        return course.lecturers  
    return None


def get_course_tutors(course_id):
    course = Course.query.get(course_id)
    if course:
        return course.tutors  
    return None

        