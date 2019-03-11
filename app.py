from flask import Flask, render_template, request, url_for, send_from_directory
from flask_restful import Resource, Api
from db import Connectdb

app = Flask(__name__)
api = Api(app)

class createstudent(Resource):
    def post(self):
        response = request.get_json()
        attendancedb = Connectdb('studentdb')
        roll_no = response['roll_no']
        name = response['name']
        stmt = "INSERT INTO solid_state_month_1 (roll_no, name) VALUES (%s, %s)" 
        data = (roll_no, name, )
        res = attendancedb.change(stmt, data)
        print(res)
        return {'message': res}, 201


class getattendance(Resource):
    def put(self, roll_no):
        attendancedb = Connectdb('studentdb')
        stmt = "UPDATE solid_state_month_1 SET day_1=%s"
        data = ('P', )
        res = attendancedb.change(stmt, data)
        print(res)
        return {'message': res}, 201

api.add_resource(createstudent, '/createstudent')
api.add_resource(getattendance, '/getattendance/<string:roll_no>')