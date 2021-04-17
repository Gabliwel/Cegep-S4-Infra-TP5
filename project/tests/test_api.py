import unittest
import unittest.mock

from myAPI import api
from myCode.customExceptions import *

class APIUnitTests(unittest.TestCase):

	def test_hello(self):
		self.assertIn("Welcome", api.hello())

	@unittest.mock.patch('myAPI.api.db')
	def test_getUsers(self, mock_db):
		mock_db.getInitialUsersFromDB.return_value = ['Bob', 'Body']
		mock_db.getNewUsersFromDB.return_value = ['Bill', 'Joe', 'Jack']
		map = api.getUsers()
		expected =  {"InitialUsers": ["Bob", "Body"], "NewUsers": ["Bill", "Jack", "Joe"]}
		self.assertCountEqual(expected, map)
		self.assertCountEqual(expected['InitialUsers'], map['InitialUsers'])
		self.assertCountEqual(expected['NewUsers'], map['NewUsers'])


	@unittest.mock.patch('myAPI.api.db')
	def test_delUsersFail(self, mock_db):
		mock_db.getInitialUsersFromDB.return_value = ['Bob', 'Body']
		mock_db.getNewUsersFromDB.return_value = ['Bill', 'Joe', 'Jack']
		with self.assertRaises(InitialUserException) as context:
			api.delUser('Bob') 
		with self.assertRaises(NonExistingUserException) as context:
			api.delUser('Al') 

	@unittest.mock.patch('myAPI.api.db')
	def test_delUsers(self, mock_db):
		mock_db.getInitialUsersFromDB.return_value = ['Bob', 'Body']
		mock_db.getNewUsersFromDB.return_value = ['Bill', 'Joe', 'Jack']
		api.delUser('Bill')
			
	@unittest.mock.patch('myAPI.api.db')
	def test_addUsersFail(self, mock_db):
		mock_db.getInitialUsersFromDB.return_value = ['Bob', 'Body']
		mock_db.getNewUsersFromDB.return_value = ['Bill', 'Joe', 'Jack']
		with self.assertRaises(UserAlreadyExistsException) as context:
			api.addUser('Bob') 
		with self.assertRaises(UserAlreadyExistsException) as context:
			api.addUser('Bill') 

	@unittest.mock.patch('myAPI.api.db')
	def test_delUsers(self, mock_db):
		mock_db.getInitialUsersFromDB.return_value = ['Bob', 'Body']
		mock_db.getNewUsersFromDB.return_value = ['Bill', 'Joe', 'Jack']
		api.addUser('Tom')
			
if __name__ == "__main__":
	unittest.main()

