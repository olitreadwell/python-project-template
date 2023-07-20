#!/usr/bin/env python3

from string_functions import return_string


def test_return_string():
    """in string_functions, function "return_string()" returns a variable of type str."""
    assert return_string() == "Hello World"
