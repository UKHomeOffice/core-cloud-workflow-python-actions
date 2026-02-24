import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_default(self):
        event = {}
        context = None
        result = lambda_handler(event, context)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'Hello, World!')

    def test_with_name(self):
        event = {'name': 'Alice'}
        context = None
        result = lambda_handler(event, context)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'Hello, Alice!')

if __name__ == '__main__':
    unittest.main()
