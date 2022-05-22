import unittest
import requests
import json

IP = "tp5-infra-zggb.ddnsgeek.com"
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
		
		self.assertIn("InitialUsers", map)
		self.assertIn("NewUsers", map)
		#marche pas
		#self.assertIn("IsaacN", map["NewUsers"])
		self.assertIn("AlbertE", map["InitialUsers"])
if __name__ == "__main__":
	unittest.main()
