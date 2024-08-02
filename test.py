import os
from dotenv import load_dotenv


def test_dotenv_variable_existence():
    load_dotenv()
    test_variable = 'BOT_TOKEN'
    token = os.getenv(test_variable)
    assert token is not None, f'Testing variable: "{test_variable}" does not exist'
    assert token != '', f'Testing variable: "{test_variable}" is set but empty'
    print(f'The environment variable "{test_variable}" exists and has some value')
