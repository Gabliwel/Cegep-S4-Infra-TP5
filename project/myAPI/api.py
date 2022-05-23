from flask import *
from myCode.customExceptions import *
from myCode import db
from myCode import version
import json

app = Flask('DB user management program')

def hello():
	return 'Ça marche?!?!? Welcome back to mega hot user program, V2.' +  version.getVersion()

@app.route('/')
def welcome(): #pragma: no cover
	return hello()


def getUsers():
    return {"InitialUsers": db.getInitialUsersFromDB(), "NewUsers": db.getNewUsersFromDB()}

@app.route('/getusers')
def route_getUsers(): #pragma: no cover
	return json.dumps({'code':'2000', 'msg': getUsers()})

def delUser(username):
	if username in db.getInitialUsersFromDB():
		raise InitialUserException(username + " is an initial user, cannot delete.")
	elif not username in db.getNewUsersFromDB():
		raise NonExistingUserException(username + " does not exist, cannot delete.")
	db.delUserFromDB(username)

@app.route('/deluser')
def route_delUser(): #pragma: no cover
	if 'username' in request.args:
		username = request.args['username']
		try:
			rep = delUser(username)
			return json.dumps({'code':'2000', 'msg':rep})
		except InitialUserException as iue:
			return make_response(json.dumps({'code':'1003', 'msg':str(iue)}), 400)
		except NonExistingUserException as neue:
			return make_response(json.dumps({'code':'1002', 'msg':str(neue)}), 400)
	else:
		return make_response(json.dumps({'code':'1000', 'msg':'param username is mandatory for deletion.'}), 400)


def addUser(username):
	if username in db.getInitialUsersFromDB():
		raise UserAlreadyExistsException(username + " already exists as initial user, cannot add it.")
	if username in db.getNewUsersFromDB():
		raise UserAlreadyExistsException(username + " already exists as new user, cannot add it.")
	db.addUserToDB(username)

@app.route('/adduser')
def route_addUser(): #pragma: no cover
	if 'username' in request.args:
		username = request.args['username']
		try:
			rep = addUser(username)
			return json.dumps({'code':'2000', 'msg':rep})
		except UserAlreadyExistsException as uaee:
			return make_response(json.dumps({'code':'1001', 'msg':str(uaee)}), 400)
	else:
		return make_response(json.dumps({'code':'1000', 'msg':'param username is mandatory for user creation.'}), 400)

if __name__ == '__main__': #pragma: no cover
	app.run(debug=True, host='0.0.0.0', port = 5555)
