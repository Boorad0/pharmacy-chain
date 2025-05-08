import pytest
import sys
from application import App

@pytest.fixture
def app(qapp):
    test_app = App()
    test_app.is_test = True 
    return test_app