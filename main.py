import unittest

from JSON_verifier import verify_input_json
from tests import TestVerifyInputJSON

if __name__ == '__main__':
    selection = input("To add a path to the file - press 1,\nto run test cases, press 2.\nConfirm your selection with enter: ")
    if selection == "1":
        input_file = input("Provide path to input file: ").replace("\"", "")
        print(verify_input_json(input_file))
    elif selection == "2":
        unittest.main()
    else:
        print("Invalid selection")
