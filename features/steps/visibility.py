from behave import *
from selenium.webdriver.common.by import By


@given(u'producent user is at "Organizations" detail page') #added page
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations/test-org/view")


@given(u'producent user is at "Tools" detail page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools/test-tool/view")


@given(u'producent user is at "Methods" detail page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods/test-method/view")


@given(u'producent user is at "Use Cases" detail page') #added use case
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases/test-use-case-23/view")


@when(u'user clicks on "State" -> "Publish"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()


@when(u'user clicks on "State" -> "Retract"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()
    context.driver.find_element(By.ID, "workflow-transition-retract").click()


@given(u'"Organizations" state is "Published"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@given(u'"Use Cases" state is "Published"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@given(u'"Tools" state is "Published"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@given(u'"Methods" state is "Published"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@given(u'"Organizations" state is "Private"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"


@given(u'"Use Cases" state is "Private"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"


@given(u'"Tools" state is "Private"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"


@given(u'"Methods" state is "Private"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"


@then(u'"Organizations" should disapper from "Organizations" list page for consument user') #url is private
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations")
    element = context.driver.find_element(By.LINK_TEXT, "Test org")
    assert element.get_attribute("class") == "contenttype-organization state-private url"


@then(u'"Use Cases" should disapper from "Use Cases" list page for consument user') #url is private
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases")
    element = context.driver.find_element(By.LINK_TEXT, "Test use case 23")
    assert element.get_attribute("class") == "contenttype-use_case state-private url"


@then(u'"Tools" should disapper from "Tools" list page for consument user') #url is private
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools")
    element = context.driver.find_element(By.LINK_TEXT, "Test tool")
    assert element.get_attribute("class") == "contenttype-tool state-private url"


@then(u'"Methods" should disapper from "Methods" list page for consument user') #url is private
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods")
    element = context.driver.find_element(By.LINK_TEXT, "Test method")
    assert element.get_attribute("class") == "contenttype-method state-private url"


@then(u'"Organizations" should apper on "Organizations" list page for consument user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations")
    element = context.driver.find_element(By.LINK_TEXT, "Test org")
    assert element.get_attribute("class") == "contenttype-organization state-published url"


@then(u'"Use Cases" should apper on "Use Cases" list page for consument user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases")
    element = context.driver.find_element(By.LINK_TEXT, "Test use case 23")
    assert element.get_attribute("class") == "contenttype-use_case state-published url"


@then(u'"Tools" should apper on "Tools" list page for consument user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools")
    element = context.driver.find_element(By.LINK_TEXT, "Test tool")
    assert element.get_attribute("class") == "contenttype-tool state-published url"


@then(u'"Methods" should apper on "Methods" list page for consument user')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods")
    element = context.driver.find_element(By.LINK_TEXT, "Test method")
    assert element.get_attribute("class") == "contenttype-method state-published url"