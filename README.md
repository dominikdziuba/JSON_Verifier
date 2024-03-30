# AWS IAM Role Policy Verifier

This Python script verifies the input JSON data for AWS IAM Role Policy. It checks if the Resource field of the input JSON contains a single asterisk.

## How to Run

1. Clone the repository to your python environment.

2. Navigate to the project directory:

3. Ensure you have Python installed.

4. Create a JSON file with your AWS IAM Role Policy data following the AWS IAM Role JSON definition and example.

5. Run the script with the following command: python .\main.py.

6. Then you will see simple context menu in your console. If you want to add path to a json file press 1, to run test cases press 2. Confirm your selection with Enter.

7. If you pressed 1, paste path to a json file (it must be .json extention), else you will see result of test cases


## File Structure
- JSON_verifier.py - Python script for verifying AWS IAM Role Policy JSON data.
- tests.py - Unit tests cases.
- main.py - Console application.

## Acknowldgements
- This project was created as a recruitment assignment for Remitly Global, Inc.