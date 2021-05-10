from time import sleep
from behave import *
from selenium.webdriver.common.by import By


def delete_page(context, try_num:int=6):
    """ Pokusí se kliknout na Actions -> Delete; občas dochází po kliku na Actions k přesměrování na stránku Contents,
        tlačítko Delete tudíž není nalezeno a dojde k vyhození výjimky a akci zkusíme znova """
    try:
        context.driver.find_element(By.XPATH, "//li[@id='plone-contentmenu-actions']/a/span[1]").click()
        context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    except:
        if try_num > 0:
            delete_page(context, try_num - 1)


@when(u'user clicks on "Actions" -> "Delete"')
def step_impl(context):
    delete_page(context)


@when(u'user confirms page deletion')
def step_impl(context):
    sleep(1.0)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'"Organizations" should disapper from "Organizations" list page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations")
    elements = context.driver.find_elements(By.LINK_TEXT, "Test org")
    assert len(elements) == 0


@then(u'"Use Cases" should disapper from "Use Cases" list page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases")
    elements = context.driver.find_elements(By.LINK_TEXT, "Test use case 23")
    assert len(elements) == 0


@then(u'"Tools" should disapper from "Tools" list page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/tools")
    elements = context.driver.find_elements(By.LINK_TEXT, "Test tool")
    assert len(elements) == 0


@then(u'"Methods" should disapper from "Methods" list page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods")
    elements = context.driver.find_elements(By.LINK_TEXT, "Test method")
    assert len(elements) == 0
