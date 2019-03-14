from flask import Flask, render_template, request, url_for, send_from_directory
from flask_restful import Resource, Api
from db import Connectdb
import os
app = Flask(__name__)
api = Api(app)

class serveresource(Resource):
    def get(self, filename):
        return send_from_directory(os.getcwd()+'/assets/', filename)


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

class getstudentdatabase(Resource):
    def get(self, tablname):
        student_db = Connectdb('studentdb')
        stmt = "SELECT * FROM ece_3b_dsp"
        data = None
        res = student_db.select(stmt, data)
        getcolnames = "SELECT * FROM information_schema.columns WHERE TABLE_NAME='ece_3b_dsp';"
        res.insert(0, student_db.select(getcolnames, None))
        return {'database': res, 'message': 'success'}, 200

api.add_resource(createstudent, '/createstudent')
api.add_resource(getattendance, '/getattendance/<string:roll_no>')
api.add_resource(serveresource, '/getaudio/<string:filename>')
api.add_resource(getstudentdatabase, '/getstuddb/<string:tablname>')