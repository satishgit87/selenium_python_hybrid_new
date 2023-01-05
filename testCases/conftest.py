import pytest
from selenium import webdriver

@pytest.fixture
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):  # this will get value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this returns browser value to setup method
    return request.config.getoption("--browser")

# ***************** PYTEST HTML REPORTS ****************
#  ******* HOOK FOR ADDING ENVIRONMENT INFO TO HTML REPOT **********
def pytest_configure(config):
    config._metadata['Project Name']='Hybrid_Framework'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester'] = 'Satish Kumar'

#  ******* HOOK FOR DELETE/MODIFY ENVIRONMENT INFO TO HTML REPOT **********
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)