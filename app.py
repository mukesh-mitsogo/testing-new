import database as db
import psycopg2
import datetime

welcome = """ Hello welcome to Mitsogo University
------------------------------
* Press 1 for Admin Login
* Press 2 for Stident Details
* Press 3 for Professor Login
------------------------------
"""
admin_options = """------------------------------
* Press 1 for Student Registration
* Press 2 for Course Registration
* Press 3 for Professor Registration
------------------------------
"""

db.create_table()


def admin_login(id, password):
    details = db.get_admin_details()
    for i in range(0, len(details)):
        if id in details[i]:
            if password in details[i]:
                return True
            else:
                return False
    return False


def getAdminName(id):
    name = db.get_admin_name(id)
    return name[0][0]


admin_welcome = """Hello Admin"""

# ----------------- Inserting Datas ---------------------------
def insert_student_details(student_id, name, dob, dep_id):
    try:
        db.insert_student_details(student_id, name, dob, dep_id)
    except psycopg2.errors.UniqueViolation:
        print("This student_id already exist")
    except psycopg2.errors.ForeignKeyViolation:
        print("No such dep_id available")
    except:
        print("something went wrong")


def insert_course_details(course_name, dep_id):
    try:
        db.insert_course_details(course_name, dep_id)
        id=db.get_courseId(course_name)
        db.insert_course_department(id,dep_id)
    except psycopg2.errors.UniqueViolation:
        id=db.get_courseId(course_name)
        try:
            db.insert_course_department(id,dep_id)
        except:
            print("error while inserting in 'course_deparment' table")
    except:
        print("error in inserting course details")


def insert_professor_details(prof_id, name, role, course_id):
    try:
        db.insert_professor_details(prof_id, name, role, course_id)
    except:
        print("error in inserting professor details")


# ----------------------------------------------------------------

# --------- Admin Work -------------
def student_registration():
    close = " "
    while close != "":
        student_id = input("Enter Roll No : ")
        name = input("Enter Name : ")
        dob = input("Enter dob in (yyyy-mm-dd) format : ")
        dep_id = int(input("Enter Department Id : "))
        insert_student_details(student_id, name, dob, dep_id)
        close = input("Press enter to exit or press anything to continue")


def course_registration():
    close = " "
    while close != "":
        course_name = input("Enter Course Name : ")
        dep_id = int(input("Enter Department Id : "))
        insert_course_details(course_name, dep_id)
        close = input("Press enter to exit or press anything to continue")


def professor_registration():
    close = " "
    while close != "":
        prof_id = input("Enter Professor Id : ")
        name = input("Enter Professor Name : ")
        role = input("Enter their role : ")
        course_id = int(input("Enter Course Id : "))
        insert_professor_details(prof_id, name, role, course_id)
        close = input("Press enter to exit or press anything to continue")


def admin_work():
    print(admin_welcome)
    adminId = input("Enter your AdminId : ")
    password = input("Enter your Password : ")
    if admin_login(adminId, password):
        admin_name = getAdminName(adminId)
        print("Welcome ", admin_name)
        admin_selection = input(admin_options)
        if admin_selection == "1":
            # Student Registration
            student_registration()
        if admin_selection == "2":
            course_registration()
        if admin_selection == "3":
            professor_registration()
    else:
        print("Wrong Password or Admin_id")


# ----------------------------------


def show_student_detail(student_id):
    try:
        student_detail = db.get_student_detail(student_id.upper())[0]
        print(
f"Your Name is {student_detail[0]}\n\
Your date of birth is {student_detail[1].strftime('%x')}\n\
Your are from {student_detail[2]} department jjc"
        )
    except:
        print("Error while fetching student Data")

def show_courses_in_a_dep(dep_id):
    try:
        pass
    except:
        pass


def student_details():
    welcome_student = """Welcome to Mitsogo University"""
    student_choices = """-------------------------------
    * Press 1 to show your details
    * Press 2 show course details
    * Press 3 to find professor
    -------------------------------
    """
    print(welcome_student)
    print(student_choices)
    student_selection = input("Enter your Choice : ")
    while student_selection in ["1", "2", "3"]:
        if student_selection == "1":
            student_id = input("Enter Your Student Id : ")
            show_student_detail(student_id)
        if student_selection == "2":
            show_courses_in_a_dep(dep_id)
        if student_selection == "3":
            show_professor(course_id)
        student_selection = input("Enter your Choice : ")


def menu():
    selection = input(welcome)
    while selection != "":
        if selection == "1":
            admin_work()
        if selection == "2":
            student_details()
        selection = input(welcome)

menu()
