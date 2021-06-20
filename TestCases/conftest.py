from selenium import webdriver
import pytest
from configurations.config import TestData


@pytest.fixture()
def setup():

    driver = webdriver.Chrome(TestData.CHORME_EXECUTABLE_PATH)
    return driver
