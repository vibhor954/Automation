import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\aasth\\Downloads\\chromedriver.exe")
    driver.get("https://insomniacookies.com/order")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver=driver
    yield
    driver.close()