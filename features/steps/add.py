from behave import *
from selenium import webdriver

@given(u'producent user clicks on "Add new" -> "Organizations"')
def step_impl(context):
    context.driver.get(f"{context.base_url}/organisations")

@when(u'user enters required "Organizations" information')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters required "Organizations" information')


@when(u'clicks on "Save" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicks on "Save" button')


@then(u'added "Organizations" is visible on "Organizations" list page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then added "Organizations" is visible on "Organizations" list page')


@given(u'producent user clicks on "Add new" -> "Use Cases"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given producent user clicks on "Add new" -> "Use Cases"')


@when(u'user enters required "Use Cases" information')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters required "Use Cases" information')


@then(u'added "Use Cases" is visible on "Use Cases" list page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then added "Use Cases" is visible on "Use Cases" list page')


@given(u'producent user clicks on "Add new" -> "Tools"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given producent user clicks on "Add new" -> "Tools"')


@when(u'user enters required "Tools" information')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters required "Tools" information')


@then(u'added "Tools" is visible on "Tools" list page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then added "Tools" is visible on "Tools" list page')


@given(u'producent user clicks on "Add new" -> "Methods"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given producent user clicks on "Add new" -> "Methods"')


@when(u'user enters required "Methods" information')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters required "Methods" information')


@then(u'added "Methods" is visible on "Methods" list page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then added "Methods" is visible on "Methods" list page')
