from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

@fixture
def ensure_driver(context):
    try:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    context.driver.implicitly_wait(15)

    yield context.driver

    context.driver.quit()

#@fixture
#def producent_login(context):
#    context.driver.

def before_all(context):
    use_fixture(ensure_driver, context)

#def before_feature(context, feature):
#    model.init(environment='test')

