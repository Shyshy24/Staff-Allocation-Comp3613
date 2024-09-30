from App.models import Admin, Course
from App.database import db

def add_admin(admin_id,admin_name):
    new_admin= Admin(AdminId=admin_id,admin_name=admin_name)
    db.session.add(new_admin)
    db.session.commit()
    return new_admin

def update_admin(admin_id,admin_name):
    admin= Admin.query.get(admin_id)
    if admin:
        admin.admin_name=admin_name
        db.session.add(admin)
        db.session.commit()
        return admin
    
def delete_admin(admin_id):
    admin= Admin.query.get(admin_id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return admin
    return None

def manage_course(course_id,admin_id):
    course= Course.query.get(course_id)
    admin= Admin.query.get(admin_id)
    if course and admin:
        course.AdminId= admin_id
        db.session.add(course)
        db.session.commit()
        return course
    return None

def get_managed_courses(admin_id):
    admin= Admin.query.get(admin_id)
    if admin:
        return Course.query.filter_by(AdminID=admin_id).all()
    return None

    