from time import sleep
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@fixture
def ensure_driver(context):
    try:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    except WebDriverException:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    context.driver.implicitly_wait(4)
    context.base_url = "http://localhost:8080/VALU3S"

@fixture
def producent_login(context):
    context.driver.get(context.base_url)
    context.driver.find_element(By.ID, "personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()

@fixture
def producent_logout(context):
    context.driver.get(context.base_url)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()


def before_all(context):
    use_fixture(ensure_driver, context)
    use_fixture(producent_login, context)
    sleep(0.6)

def after_all(context):
    use_fixture(producent_logout, context)
    context.driver.quit()
