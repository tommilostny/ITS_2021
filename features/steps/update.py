from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'"Organizations" edit page is visible to producent user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations/test-org/edit")


@given(u'"Tools" edit page is visible to producent user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools/test-tool/edit")


@given(u'"Use Cases" edit page is visible to producent user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases/test-use-case-23/edit")


@given(u'"Methods" edit page is visible to producent user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods/test-method/edit")


@when(u'user updates "Organizations" text field')
def step_impl(context):
    element = context.driver.find_element(By.ID, "form-widgets-organization_acronym")
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys("NEW_ACRONYM")


@then(u'updated information should replace old information on "Organizations" detail page')
def step_impl(context):
    assert context.driver.find_element(By.ID, "form-widgets-organization_acronym").text == "NEW_ACRONYM"


@when(u'user updates "Use Cases" text field')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-description").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-description").send_keys("Tese use case summary")


@then(u'updated information should replace old information on "Use Cases" detail page')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".documentDescription").text == "Tese use case summary"


@when(u'user updates "Tools" text field')
def step_impl(context):
    element = context.driver.find_element(By.ID, "form-widgets-tool_purpose")
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys("NEW PURPOSE")


@then(u'updated information should replace old information on "Tools" detail page')
def step_impl(context):
    assert context.driver.find_element(By.ID, "form-widgets-tool_purpose").text == "NEW PURPOSE"


@when(u'user updates "Methods" text field')
def step_impl(context):
    element = context.driver.find_element(By.ID, "form-widgets-method_purpose")
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys("New updated method purpose that is much more important")


@then(u'updated information should replace old information on "Methods" detail page')
def step_impl(context):
    element = context.driver.find_element(By.ID, "form-widgets-method_purpose")
    assert element.text == "New updated method purpose that is much more important"
