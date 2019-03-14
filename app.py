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
    def put(self, roll_no, date):
        attendancedb = Connectdb('studentdb')
        stmt = "UPDATE ece_3b_dsp SET `"+date+"` =1 WHERE roll_no=%s"
        data = (roll_no, )
        res = attendancedb.change(stmt, data)
        print(res)
        return {'message': res, 'code': 201}, 201

class getstudentdatabase(Resource):
    def get(self, tablname):
        student_db = Connectdb('studentdb')
        stmt = "SELECT * FROM ece_3b_dsp"
        data = None
        res = student_db.select(stmt, data)
        getcolnames = "SELECT COLUMN_NAME FROM information_schema.columns WHERE TABLE_NAME='ece_3b_dsp';"
        cols = student_db.select(getcolnames, None)
        colnames = [x[0] for x in cols]
        res.insert(0, colnames)
        return {'database': res, 'message': 'success'}, 200

class createclass(Resource):
    def put(self, date):
        student_db = Connectdb('studentdb')
        stmt = "ALTER TABLE ece_3b_dsp ADD COLUMN `"+date+"` TINYINT(1) NULL"
        data = None
        res = student_db.change(stmt, data)
        return {'message': res}, 201

class deleteclass(Resource):
    def put(self, date):
        student_db = Connectdb('studentdb')
        stmt = "SHOW COLUMNS FROM ece_3b_dsp like '"+date+"'"
        res = student_db.select(stmt, None)
        if len(res) == 0:
            return {'message': 'This class does not exist!'}, 404
        else:
            stmt2 = "ALTER TABLE ece_3b_dsp DROP COLUMN `"+date+"`"
            res2 = student_db.change(stmt2, None)
            return {'message': res2}, 200




api.add_resource(createstudent, '/createstudent')
api.add_resource(getattendance, '/getattendance/<string:date>/<string:roll_no>')
api.add_resource(serveresource, '/getaudio/<string:filename>')
api.add_resource(getstudentdatabase, '/getstuddb/<string:tablname>')
api.add_resource(createclass, '/createclass/<string:date>')
api.add_resource(deleteclass, '/deleteclass/<string:date>')