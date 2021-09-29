import psycopg2

connection = psycopg2.connect("user=ehdrzqyr password=wMOcM_4F_Chxqg6F5ASPzVmj_qghUI1w dbname=ehdrzqyr host=surus.db.elephantsql.com")


CREATE_STUDENTS = "CREATE TABLE IF NOT EXISTS students(student_id VARCHAR(10) PRIMARY KEY,\
                name VARCHAR(30) NOT NULL,\
                dob DATE NOT NULL,\
                dep_id INT REFERENCES departments(dep_id));"

CREATE_COURSES = "CREATE TABLE IF NOT EXISTS courses(course_id SERIAL PRIMARY KEY,\
                  course_name VARCHAR(30) UNIQUE);"

CREATE_PROFESSORS = "CREATE TABLE IF NOT EXISTS professors(prof_id VARCHAR(10) PRIMARY KEY,\
                     name VARCHAR(30) NOT NULL,\
                     role TEXT,\
                     course_id INT REFERENCES courses(course_id));"

CREATE_DEPARTMENTS = "CREATE TABLE IF NOT EXISTS departments(dep_id SERIAL PRIMARY KEY,\
                      dep_name TEXT);"
                    
CREATE_ADMIN = "CREATE TABLE IF NOT EXISTS admin(admin_id VARCHAR(10) PRIMARY KEY,\
                user_name TEXT NOT NULL,\
                password TEXT NOT NULL );"
CREATE_COURSE_DEPARTMENT = "CREATE TABLE IF NOT EXISTS course_department(\
                            course_id INT REFERENCES courses(course_id),dep_id INT REFERENCES departments(dep_id));"

GET_ADMIN_DETAILS = "SELECT * FROM admin"

GET_NAME = "SELECT user_name FROM admin WHERE admin_id = %s"


INSERT_STUDENT_DETAILS = "INSERT INTO students(student_id,name,dob,dep_id) VALUES (%s,%s,%s,%s);"
INSERT_COURSE_DETAILS = "INSERT INTO courses(course_name) VALUES (%s);"
INSERT_PROFESSOR_DETAILS="INSERT INTO professors(prof_id,name,role,course_id) VALUES (%s,%s,%s,%s);"
INSERT_COURSE_DEPARTMENT = "INSERT INTO course_department(course_id,dep_id) VALUES (%s,%s);"

GET_STUDENT_DETAIL = "SELECT s.name,s.dob,d.dep_name FROM students s\
                      JOIN departments d ON d.dep_id = s.dep_id  \
                      WHERE s.student_id = %s ;"
GET_COURSE_ID = "SELECT course_id FROM courses\
                WHERE course_name = %s ;"

def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_DEPARTMENTS)
            cursor.execute(CREATE_ADMIN)
            cursor.execute(CREATE_STUDENTS)
            cursor.execute(CREATE_COURSES)
            cursor.execute(CREATE_PROFESSORS)
            cursor.execute(CREATE_COURSE_DEPARTMENT)

def get_admin_details():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ADMIN_DETAILS)
            return cursor.fetchall()

def get_admin_name(adminid):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_NAME,(adminid,))
            return cursor.fetchall()

def insert_student_details(student_id,name,dob,dep_id):
     with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_STUDENT_DETAILS,(student_id,name,dob,dep_id))

def insert_course_details(course_name,dep_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_COURSE_DETAILS,(course_name,))


def get_courseId(course_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_COURSE_ID,(course_name,))
            course_id = cursor.fetchall()[0][0]
            return course_id

def insert_course_department(course_id,dep_id):
   with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_COURSE_DEPARTMENT,(course_id,dep_id))


def insert_professor_details(prof_id,name,role,course_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_PROFESSOR_DETAILS,(prof_id,name,role,course_id))


def get_student_detail(student_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_STUDENT_DETAIL,(student_id,))
            return cursor.fetchall()


            
