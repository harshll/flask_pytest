

# from requests import request
from sample import Student, app
import pytest
from flask_fixtures import FixturesMixin
# import requests

"""
App Configuration
"""
@pytest.fixture
def client():
    app.config.update({'TESTING': True})

    with app.test_client() as client:
        yield client
        
"""
Tset Case For Get Student Data
"""        
def test_get_student_api(client):
    URL = "http://127.0.0.1:5000/get"
    responses = client.get(URL)
    assert responses.status_code == 400


"""
Test Case For Create Student Data
"""
def test_post_student_api(client):
    URL = "http://127.0.0.1:5000/add_student"
    data = {
        "name" : "Hemang Gowshami",
        "roll_number" : 111111
    }
    response = client.post(URL,json=data)
    assert response.status_code == 200
    # assert response.dict() == data
    
"""
Test Case For Update Student Data
"""
def test_put_student_api(client):
    URL="http://127.0.0.1:5000/update/2"
    data= {
        "name" : "Hemang Gowshami",
        "roll_number" : 111111
    }
    response=client.put(URL,json=data)
    assert response.status_code == 200
    
    

    
    #or response.status_code == 404
    # assert response.status_code == 200
# @pytest.mark.parametrize(get_student)
# def test_get_student_api():
#     URL = "http://127.0.0.1:5000/get"
#     responses = requests.get(URL)
#     assert responses.status_code == 400


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


        
        
        
# configure_routes=app

# def func(x):
#     return x + 1

# def test_answer():
#     assert func(4) == 5


# def test_answer():
#     assert func(3) == 5



# @pytest.fixture


# @pytest.fixture
# def test_get_route(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/get'
    
#     # student = db.session.query(Student).all()
#     # data = jsonify({'data': [{'id': student.id, 'name': student.name , 'roll_number':student.roll_number} for student in student]})
#     # response = client.get(url,student)
#     # assert response.status_code == 200
    
# @pytest.fixture
# def test_post_route_success(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/add_student'
    
#     models = Student()
#     pass_request_data = {
#         "name" : "Harshal",
#         "roll_number" : 12
#     }
#     student = (models.name,models.roll_number)
#     response = client.post(url,student)
#     assert response.status_code == 200
    
# def test_post_route_fail(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/add_student'
    
#     pass_request_data = {
#         "name" : "Harshal",
#         "roll_number" : 12
#     }
    
#     response = client.post(url,data=request.json(pass_request_data))
#     assert response.status_code == 200
    
# def test_delete_route_success(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/delete/<int:id>'
    
#     response = client.delete(url,data=id)
#     assert response.status_code == 200
    
# def test_delete_route_fail(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/delete/<int:id>'
    
#     response = client.delete(url,data=id)
#     assert response.status_code == 404
    
# def test_update_route_success(client):
#     # app = Flask(__name__)
#     # configure_routes(app)
#     # client = app.test_client()
#     url = '/update/<int:id>'
    
#     pass_request_data = {
#         "name" : "Harshal",
#         "roll_number" : 12
#     }
    
#     response = client.patch(url,data=request.json(pass_request_data))
#     assert response.status_code == 200