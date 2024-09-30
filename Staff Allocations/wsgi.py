import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 


@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Admin Commands
'''
admin_cli = AppGroup('admin', help='Admin object commands')

@admin_cli.command("create", help="Creates an admin")
@click.argument("admin_name", default="admin")
@click.argument("password", default="adminpass")
def create_admin_command(admin_name, password):
    from App.controllers import create_admin
    create_admin(admin_name, password)
    print(f'Admin {admin_name} created!')

@admin_cli.command("list", help="Lists all admins")
def list_admin_command():
    from App.controllers import get_all_admins_json
    print(get_all_admins_json())

app.cli.add_command(admin_cli)

'''
Course Commands
'''
course_cli = AppGroup('course', help='Course object commands')

@course_cli.command("create", help="Creates a course")
@click.argument("course_name", default="New Course")
@click.argument("course_description", default="This is a new course.")
@click.argument("admin_id", default=1)
def create_course_command(course_name, course_description, admin_id):
    from App.controllers import create_course
    create_course(course_name, course_description, admin_id)
    print(f'Course {course_name} created!')

@course_cli.command("list", help="Lists all courses")
def list_course_command():
    from App.controllers import get_all_courses_json
    print(get_all_courses_json())

app.cli.add_command(course_cli)

'''
Lecturer Commands
'''
lecturer_cli = AppGroup('lecturer', help='Lecturer object commands')

@lecturer_cli.command("create", help="Creates a lecturer")
@click.argument("lecturer_name", default="lecturer")
@click.argument("lecturer_role", default="Professor")
def create_lecturer_command(lecturer_name, lecturer_role):
    from App.controllers import create_lecturer
    create_lecturer(lecturer_name, lecturer_role)
    print(f'Lecturer {lecturer_name} created!')

@lecturer_cli.command("list", help="Lists all lecturers")
def list_lecturer_command():
    from App.controllers import get_all_lecturers_json
    print(get_all_lecturers_json())

app.cli.add_command(lecturer_cli)

'''
Tutor(TA) Commands
'''
tutor_cli = AppGroup('tutor', help='Tutor object commands')

@tutor_cli.command("create", help="Creates a tutor")
@click.argument("ta_name", default="TA")
@click.argument("ta_role", default="Teaching Assistant")
def create_tutor_command(ta_name, ta_role):
    from App.controllers import create_tutor
    create_tutor(ta_name, ta_role)
    print(f'Tutor {ta_name} created!')

@tutor_cli.command("list", help="Lists all tutors")
def list_tutor_command():
    from App.controllers import get_all_tutors_json
    print(get_all_tutors_json())

app.cli.add_command(tutor_cli)


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)