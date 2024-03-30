import unittest
from unittest.mock import patch
from io import StringIO
import json
from JSON_verifier import verify_input_json

class TestVerifyInputJSON(unittest.TestCase):
    def test_valid_json_no_asterisk(self):
        # Valid JSON without an asterisk in the Resource field
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "AWS",  # Updated to match AWS::IAM::Role Policy
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "arn:aws:iam::account-id-without-hyphens:role/some-role-name"
                    }
                ]
            }
        }
        with patch('builtins.open', return_value=StringIO(json.dumps(json_data))):
            result = verify_input_json("dummy_file.json")
            self.assertTrue(result)

    def test_valid_json_with_asterisk(self):
        # Valid JSON with an asterisk in the Resource field
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "*"
                    }
                ]
            }
        }
        with patch('builtins.open', return_value=StringIO(json.dumps(json_data))):
            result = verify_input_json("dummy_file.json")
            self.assertFalse(result)

    def test_missing_resource_field(self):
        # Missing Resource field
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ]
                    }
                ]
            }
        }
        with patch('builtins.open', return_value=StringIO(json.dumps(json_data))):
            result = verify_input_json("dummy_file.json")
            self.assertFalse(result)

    def test_invalid_json_format(self):
        # Invalid JSON format
        with patch('builtins.open', return_value=StringIO("invalid_json")):
            result = verify_input_json("dummy_file.json")
            self.assertFalse(result)

    def test_invalid_statement_structure(self):
        # Invalid statement structure
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": "not a list"
            }
        }
        with patch('builtins.open', return_value=StringIO(json.dumps(json_data))):
            result = verify_input_json("dummy_file.json")
            self.assertFalse(result)

    def test_invalid_resource_type(self):
        # Invalid resource type
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": 123  # Invalid type, should be string
                    }
                ]
            }
        }
        with patch('builtins.open', return_value=StringIO(json.dumps(json_data))):
            result = verify_input_json("dummy_file.json")
            self.assertFalse(result)



