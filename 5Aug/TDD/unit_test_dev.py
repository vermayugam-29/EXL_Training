import pytest
from dev import validate_user_id_password

#python -m pytest unit_test_dev.py -v


def test_valid_credentials():
    assert validate_user_id_password("user01", "Yugam@123") is True

def test_short_password():
    assert validate_user_id_password("user01", "Yug!") is False

def test_short_user_id():
    assert validate_user_id_password("usr", "Yugam!123") is False

def test_password_no_digit():
    assert validate_user_id_password("user01", "Yugam!@m") is False

def test_password_no_uppercase():
    assert validate_user_id_password("user01", "yugam@1234") is False

def test_password_no_lowercase():
    assert validate_user_id_password("user01", "YUGAM@123") is False

def test_password_no_special_char():
    assert validate_user_id_password("user01", "Yugam12345") is False

def test_edge_case_min_length():
    assert validate_user_id_password("user01", "Yuga@12") is False

def test_edge_case_user_id_length():
    assert validate_user_id_password("user1", "Yugam@1234!") is True
