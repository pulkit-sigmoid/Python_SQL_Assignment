import pytest
from data import data
from connection import connection

# If data return true that means I am able to read all data but if it returns none that means my database has some error
def testing_the_data():
    assert data() == True

# If connection return true that mean my connection is successful but if it returns none that means my conn failed
def testing_the_connection():
    assert connection() == True


