import pytest
from selenium import webdriver

driver=None


@pytest.fixture()
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.magicbricks.com/")
    request.cls.driver = driver
    yield
    driver.quit()

