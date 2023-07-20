#!/usr/bin/env python3

from User import User


def test_user():
    """in User, class "User()" returns a variable of type User."""

    test_user = User()
    assert test_user.name == "Joanna Doe"
    assert test_user.email == "joanna.doe@mail.com"
