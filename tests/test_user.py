# correct syntax for a from import
from src.user import User

def test_user():
    assert True

def test_user_name():
    user = User()
    assert user.user_name == "John Doe"