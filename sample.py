
# from asyncio import events
import json
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,request,redirect
import redis
from sqlalchemy.orm.exc import NoResultFound
# from flask_fixtures import FixturesMixin
# import pytest
from sqlalchemy import event
from datetime import datetime
# from flask_migrate import Migrate,MigrateCommand
# from rq import worker,Queue,Connection



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:harshal@localhost/csv_db2'
db = SQLAlchemy(app)

# redis_url = ('REDISTOGO_URL' , 'redis://localhost:6379')
# conn = redis.from_url(redis_url)
# redis_cache = redis.Redis(host='localhost', port=6379, db=0, password="")

if __name__ == "__main__":
	app.run("127.0.0.1", port="5001", debug=True)

class Student(db.Model):
    __tablename__ = "students"
    id           = db.Column(db.Integer(),primary_key=True)
    name         = db.Column(db.String(length=30), nullable=True)
    roll_number  = db.Column(db.Integer(), nullable=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    
@event.listens_for(Student.__table__,'after_create')
def create_student(*args,**kwargs):
    with open('students.json') as file:
        data=json.load(file)
    db.session.add(Student(),data)
    db.session.commit()

# def func(x):
#     return x + 1
# with open('students.json') as file:
#     data=json.load(file)
# def insert_data(target,app,data,**kw):
#     app.execute(target.insert(),data)
#     event.listen(Student.__tablename__,'after_create',insert_data)

# class configure_routes(app):


@app.route('/get',methods = ['GET'])
def get_student():
    """
    Get Student 
    """
    
    # Get Student
    student_all = db.session.query(Student).all()

    response = jsonify({
        'status': 'SUCCESS',
        'code': 900,
        'data': [{'id': student.id, 'name': student.name , 'roll_number':student.roll_number} for student in student_all]
    })
    
    return response



@app.route('/add_student' , methods = ['POST'])
def post():
    data=request.json
    create_student=Student(
        name=data['name'],
        roll_number=data['roll_number'],
    )
    db.session.add(create_student)
    db.session.commit()
    response = (
            jsonify(
            {
                    "status": "SUCCESS",
                    "code": 900,
                    "message": "Student Create Successfully!!" ,
                }
            ),
            200,
        )
    return response




@app.route('/delete/<int:id>',methods=['GET','DELETE'])
def delete(id):
    student = Student.query.filter_by(id=id).first()
    if not student:
        raise NoResultFound
        
    db.session.delete(student)
    db.session.commit()
    response =  (jsonify({
        'status': 'SUCCESS',
        'code': 900,
        'message': 'Student Deleted!',
    }),200)
    
    return response





        
@app.route('/update/<int:id>',methods = ['GET','PUT'])
def update(id):
    try:
        data=request.json
        student = db.session.query(Student).filter(Student.id == id).first()
        print(f'\n\n\n\n\n\n{student}')
        if student:
            student=({
                Student.name : data['name'],
                Student.roll_number : data['roll_number']
                })
            db.session.commit()
            
            # student1 = Student.query.filter_by(id=id).first()
            response =  (jsonify({    
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Student Updated!'
            }),200)
            # 2
            return response
            
        else:
            response =  (jsonify({
                
                'status': 'ERROR',
                'code': 404,
                'message': 'Student not found!'
            }),404)
            # 3
            return response
    except:
        return 'Error'
    

# class TestMyApp(pytest.TestCase,FixturesMixin):
#     fixtures = ['students.json']

#     # Specify the Flask app and database we want to use for this set of tests
#     app = app
#     db = db

#     # Your tests go here

#     def test_add_student(self):
#         # Add another student on the fly
#         students = Student()
#         students.name = 'George'
#         students.roll_number = 10
#         self.db.session.add(students)
#         self.db.session.commit()


# def put(self,pass_id):
#         try:
#             #Validate
#             store.RoyalPassJson(request.json)

#             royalpass = request.json
#             royalpass['updated_at'] = datetime.utcnow()
#             royalpasses = db.session.query(Royalpass).filter_by(id = pass_id)           
#             royalpasses.update(
#                 royalpass
#             )
#             db.session.flush()
#             db.session.commit()
            
#             royalpasses = royalpasses.first()


#             if not royalpasses:
#                 raise NoResultFound

#             response =  (jsonify({
#                         'status': 'SUCCESS',
#                         'code': 900,
#                         'message': 'Royal pass Updated!',
#                         'data':{
#                             'id':royalpasses.id,
#                             'description':royalpasses.description,
#                             'logo':royalpasses.logo,
#                             'tokens':royalpasses.tokens,
#                             'created_at':royalpasses.created_at,
#                             'updated_at':royalpasses.updated_at,
#                         }
#                     }),200)

 

# def delete(self,badge_id):
#         try:    
            
#             badge = db.session.query(models.Badges).filter_by(id =badge_id ).first()
#             if not badge:
#                 raise NoResultFound

#             db.session.delete(badge)
#             db.session.commit()

#             response =  (jsonify({
#                         'status': 'SUCCESS',
#                         'code': 900,
#                         'message': 'Badge Deleted!',
#                     }),200)








    # if request.method == 'POST':
    #     name = request.form['name']
    #     roll_number = request.form['roll_number']
        
    #     student = Student(name=name,roll_number = roll_number)
    #     db.session.add(student)
    #     db.session.commit()
    #     return render_template('index.html')
  









# def add_user_idenity():
#     """
#     Add custom user identity
#     """

#     try:
#         # Get the user information
#         user_id = get_jwt_identity()

#         # Validate the data
#         user_validation.custom_user_identity(request.json)

#         # Get the data
#         params = request.json

#         # Get User
#         user_data = User.query.filter(User.id == user_id).first()

#         if user_data is not None:

#             identity = Identity(
#                 identity=params['identity'], added_user_id=user_id, is_enabled=True)

#             # Commit
#             db.session.add(identity)
#             db.session.commit()

#             response = (
#                 jsonify(
#                     {
#                         "status": "SUCCESS",
#                         "code": 900,
#                         "message": message.IDENTITY_ADDED,
#                     }
#                 ),
#                 200,
#             )
#         else:
#             response = (
#                 jsonify(
#                     {
#                         "status": "SUCCESS",
#                         "code": 901,
#                         "message": message.USER_NOT_FOUND,
#                     }
#                 ),
#                 200,
#             )







    
# def get_student():
    
#     student_all = db.session.query(Student).all()
    
#     students = [
#         {
#             'id':student_all.id,
#             'name':student_all.name,
#             'roll_number':student.number
#         }
#         for student in students
#     ]
    # try:
    #     if redis_cache.get('student'):
    #         print("Getting from cache")
    #         students = redis_cache.get('student')
    #         return "getting from cache"
    #     else:
    #         redis_cache.set(3,10,ex=3600)
    #         return "setted to cache"
    # except:
    #     return "not getting from cache"
        
    # student_cache_key="student_{}_{}_{}"
    # if redis_cache.get(student_cache_key) is None:
    #     students = db.session.query(students.id.label('id'),students.name,students.roll_number)
    #     redis_cache.set(student_cache_key,json.dumps(students))
    #     print('\n\n\n\n\n-----from db-----\n\n\n\n\n')
    # else:
    #     print('\n\n\n\n\n-----from redis-----\n\n\n\n\n')
    #     students=json.loads(redis_cache.get(student_cache_key))
    #     # final_data=[]
    #     # for student in key:
    #     #     student_data = {}
    #     #     student_data['name'] = student.name
    #     #     student_data['roll_number'] = student.roll_number
    #     #     final_data.append(student_data)
    #     # return redis_cache.get(key)
    # return {'data':student_all},{"students":students}





# @app.route('/data/create' , methods = ['GET','POST'])
# def post():
#     if request.method == 'POST':
#         name = request.form['name']
#         roll_number = request.form['roll_number']
        
#         student = Student(name=name,roll_number = roll_number)
#         db.session.add(student)
#         db.session.commit()
#         return render_template('index.html')
  
  
  
  









