# attendance_app
API for the QR based class attendance app built using flutter
#####    Baseurl: https://attandance-app.herokuapp.com/


## /createstudent POST
###     Creates a student entry to the database
###     Consumes: 
####     application/json
         Sample: {"roll_no": 33, "univ_roll_no": 10900316057, "reg_no": 161090110307, "name": "John Doe"}
###     Produces: 
####     application/json 
         Sample: {"message" : "some message"}, 201 (on success)
## /createclass/{string:date} PUT
###     Creates a class entry for a particular date
###     Consumes: 
####     Date (String) in path param
###     Produces: 
####     application/json
         Sample: {"message" : "some message"}, 201 (on success)
         
## /deleteclass/{string:date} PUT
###     Checks if a class exists , if yes, deletes the class
###     Consumes: 
####     Date (String) in path param
###     Produces: 
####     application/json
         Sample: {"message" : "some message"}, 201 (on success), 404 (on failure)
         
## /getattendance/{string:date}/{string:roll_no}  PUT
###     Gives attendance to a particular student for a particular date
###     Consumes: 
####     Date(String) and Roll No(String) in path param
###     Produces: 
####     application/json
         Sample: {"message" : "some message"}, 201 (on success)
         
## /getstuddb/{string:tablename}    GET
###     Returns the table corresponding to a section
####     Table name structure: {dept_name}__{yearname(int)+section}__{subject} 
####     e.g. ece_3b_dsp == dept ece, 3rd year, section b, digital signal processing
###     Consumes: 
####     Tablename(String) in path param
###     Produces: 
####     application/json
         Sample: {"database" : table, "message": "success"}, 200 OK
## /validatelogin POST
###      Validate teacher login through api
###      Consumes: 
####     application/json
          Sample: {"name": "Snehangshu Bhattacharya", "hash": "h9gf4w7t4t943hgwhg9f"}
###      Produces:
####     application/json
          Sample: {"success": True}, 200 or {"success": False}, 401 (password wrong) or {"success": False}, 403 (username does not exist)

