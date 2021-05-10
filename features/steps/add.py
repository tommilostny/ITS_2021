from behave import *
from selenium.webdriver.common.by import By


def add_new_page_base(page:str, context):
    context.driver.find_element(By.CSS_SELECTOR, ".icon-plone-contentmenu-factories").click()
    element = context.driver.find_elements(By.ID, page)
    if len(element):
        element[0].click()
    else:
        context.driver.find_element(By.ID, f"form-field-{page}").click()
        context.driver.find_element(By.NAME, "form.button.Add").click()


@given(u'producent user clicks on "Add new" -> "Organizations"')
def step_impl(context):
    add_new_page_base("organization", context)


@when(u'user enters required "Organizations" information')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test org")
    context.driver.find_element(By.ID, "form-widgets-organization_acronym").click()
    context.driver.find_element(By.ID, "form-widgets-organization_acronym").send_keys("TOG")


@when(u'clicks on "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'added "Organizations" detail page is accessible')
def step_impl(context):
    context.driver.get(f"{context.base_url}/test-org/view")


@given(u'producent user clicks on "Add new" -> "Use Cases"')
def step_impl(context):
    add_new_page_base("use_case", context)


@when(u'user enters required "Use Cases" information')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test use case 23")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test use case 23 description</p>'}", element)
    context.driver.switch_to.default_content()


@then(u'added "Use Cases" detail page is accessible')
def step_impl(context):
    context.driver.get(f"{context.base_url}/test-use-case-23/view")


@given(u'producent user clicks on "Add new" -> "Tools"')
def step_impl(context):
    add_new_page_base("tool", context)


@when(u'user enters required "Tools" information')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Test tool")
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").click()
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("Test tool purpose")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test tool description</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test tool strengths</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test tool limitations</p>'}", element)
    context.driver.switch_to.default_content()


@then(u'added "Tools" detail page is accessible')
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools/test-tool/view")


@given(u'producent user clicks on "Add new" -> "Methods"')
def step_impl(context):
    add_new_page_base("method", context)


@when(u'user enters required "Methods" information')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test method")
    context.driver.find_element(By.ID, "form-widgets-method_purpose").click()
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("Test method purpose")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test method description</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test method strengths</p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test method limitations</p>'}", element)
    context.driver.switch_to.default_content()


@then(u'added "Methods" detail page is accessible')
def step_impl(context):
    context.driver.get(f"{context.base_url}/test-method/view")
