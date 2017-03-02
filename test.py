from rest_api import app
import unittest
import json


class FlaskTestCase(unittest.TestCase):
    def test_get_all(self):
        print("#############################################")
        print("############## started test case ############")
        print("#############################################")
        tester = app.test_client(self)
        response = tester.get('/employees', content_type='json')
        print(response)
        self.assertEqual(response.status_code, 200)
        print("#############################################")
        print("############## completed test case ##########")
        print("#############################################")

    """def test_index(self):
        tester  = app.test_client(self)
        response = tester.get('/employee/getAll',content_type = 'text/html')
        self.assertEqual(response.status_code,200)
        print("Done with test!!!!")

    def test_index(self):
        tester  = app.test_client(self)
        response = tester.get('/employee/getAll',content_type = 'text/html')
        self.assertEqual(response.status_code,200)
        print("Done with test!!!!")
    def test_index(self):
        tester  = app.test_client(self)
        response = tester.get('/employee/getAll',content_type = 'text/html')
        self.assertEqual(response.status_code,200)
        print("Done with test!!!!")"""


if __name__ == "__main__":
    unittest.main()
