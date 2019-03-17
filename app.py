from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from db import Connectdb
import os
import json
app = Flask(__name__)
api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

class serveresource(Resource):
    def get(self, filename):
        return send_from_directory(os.getcwd()+'/assets/', filename)


class createstudent(Resource):
    def post(self):
        response = request.get_json()
        attendancedb = Connectdb('studentdb')
        roll_no = response['roll_no']
        name = response['name']
        univ_roll_no = response['univ_roll_no']
        reg_no = response['reg_no']
        stmt = "INSERT INTO ece_3b_dsp (roll_no, univ_roll_no, reg_no, name) VALUES (%s, %s, %s, %s)"
        data = (roll_no, univ_roll_no, reg_no, name, )
        res = attendancedb.change(stmt, data)
        print(res)
        return {'message': res}, 201


class getattendance(Resource):
    def put(self, publichash, roll_no, date):
        with open('auth.json') as authjson:
            jsondata = json.load(authjson)
            privatehash = jsondata['token']
            authjson.close()
        if privatehash == publichash:
            attendancedb = Connectdb('studentdb')
            stmtchk = "SELECT `"+date+"` FROM ece_3b_dsp WHERE roll_no=%s"
            datachk = (roll_no, )
            reschk = attendancedb.select(stmtchk, datachk)
            if reschk[0][0] == None:
                stmt = "UPDATE ece_3b_dsp SET `"+date+"` =1 WHERE roll_no=%s"
                data = (roll_no, )
                res = attendancedb.change(stmt, data)
                print(res)
                return {'message': res, 'code': 201}, 201
            else:
                return {'message': 'You got your attendance already!'}, 400
        else:
            return {'message': 'Hash mismatch! Dont try to copy QRs ;)'}, 404


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

class validatelogin(Resource):
    def post(self):
        teacher_db = Connectdb('teacherdb')
        logincreds = request.get_json()
        usrname = logincreds['name']
        usrhash = logincreds['hash']
        stmtchk = "SELECT name FROM teachertabl WHERE name LIKE %s"
        chkusr = teacher_db.select(stmtchk, (usrname, ))
        try:
            if chkusr[0][0] == usrname:
                stmt = "SELECT hash FROM teachertabl WHERE name=%s"
                data = (usrname, )
                tablhash = teacher_db.select(stmt, data)
                if tablhash[0][0] == usrhash:
                    return {'success': True}, 200
                else:
                    return {'success': False}, 401
            else:
                return {'success': False}, 403
        except IndexError:
            return {'success': False}, 403

class usrregister(Resource):
    def post(self):
        teacher_db = Connectdb('teacherdb')
        registercreds = request.get_json()
        usrname = registercreds['name']
        usrhash = registercreds['hash']
        print(usrname, usrhash)
        stmt = "INSERT INTO teachertabl (name, hash) VALUES (%s, %s)"
        data = (usrname, usrhash, )
        res = teacher_db.change(stmt, data)
        return {'message': res}, 201

api.add_resource(validatelogin, '/validatelogin')
api.add_resource(usrregister, '/usrregister')
api.add_resource(createstudent, '/createstudent')
api.add_resource(getattendance, '/getattendance/<string:publichash>/<string:date>/<string:roll_no>')
api.add_resource(serveresource, '/getaudio/<string:filename>')
api.add_resource(getstudentdatabase, '/getstuddb/<string:tablname>')
api.add_resource(createclass, '/createclass/<string:date>')
api.add_resource(deleteclass, '/deleteclass/<string:date>')