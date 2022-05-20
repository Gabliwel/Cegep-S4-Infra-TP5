import unittest
import requests
import json
from myAPI import api

IP = "0.0.0.0"
PORT = "5555"
URL = "http://" + IP + ":" + PORT

class APIDeployTest(unittest.TestCase):

	def test_home(self):
		response = requests.get(URL + "/")
		self.assertEqual(200, response.status_code)

	def test_getUsers(self):
		response = requests.get(URL + "/getusers")
		self.assertEqual(200, response.status_code)
		map = json.loads(response.content.decode('utf-8'))
		map = map['msg']
		print("----------Map----------")
		print(map)
		print("----------expected----------")
		expected =  {"InitialUsers": ["Bob", "Body"], "NewUsers": ["Bill", "Jack", "Joe"]}
		print(expected)
		self.assertCountEqual(expected, map)
		self.assertCountEqual(expected['InitialUsers'], map['InitialUsers'])
		self.assertCountEqual(expected['NewUsers'], map['NewUsers'])

	def test_delUserFail1(self):
		response = requests.get(URL + "/deluser?username=Bob")
		self.assertEqual(400, response.status_code)
		
	def test_delUserFail2(self):
		response = requests.get(URL + "/deluser?username=Al")
		self.assertEqual(400, response.status_code)
		
	def test_delUser(self):
		response = requests.get(URL + "/deluser?username=Joe")
		self.assertEqual(200, response.status_code)
		
		response = requests.get(URL + "/getusers")
		self.assertEqual(200, response.status_code)
		map = json.loads(response.content.decode('utf-8'))
		map = map['msg']
		
		self.assertNotIn('Joe', map['NewUsers'])
	
	def test_addUserFail1(self):
		response = requests.get(URL + "/adduser?username=Bob")
		self.assertEqual(400, response.status_code)

	def test_addUserFail2(self):
		response = requests.get(URL + "/adduser?username=Bill")
		self.assertEqual(400, response.status_code)
		
	def test_addUser(self):
		response = requests.get(URL + "/adduser?username=Tom")
		self.assertEqual(200, response.status_code)	
		
		response = requests.get(URL + "/getusers")
		self.assertEqual(200, response.status_code)
		map = json.loads(response.content.decode('utf-8'))
		map = map['msg']
		self.assertIn('Tom', map['NewUsers'])
		
if __name__ == "__main__":
	unittest.main()
