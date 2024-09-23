# assertion.py
from behave import then
import logging
from pyjab.jabdriver import JABDriver

logging.basicConfig(level=logging.INFO)

@then('the user validates if button "{textOption}" is enabled')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"    
    try:
        element = jabdriver.find_element_by_xpath(location)
        assert element.is_enabled(), f"Button '{textOption}' is not enabled but should be."    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

@then('the user validates if button "{textOption}" is disabled')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"    
    try:
        element = jabdriver.find_element_by_xpath(location)       
        assert not element.is_enabled(), f"Button '{textOption}' is enabled but should be disabled."    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

@then('the user validates if "{textOption}" checkbox is not selected')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"    
    try:
        element = jabdriver.find_element_by_xpath(location)
        assert not element.is_checked(), f"Checkbox '{textOption}' is selected, but it should not be."    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

@then('the user validates if "{textOption}" checkbox is selected')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"  
    try:
        element = jabdriver.find_element_by_xpath(location)
        assert element.is_checked(), f"Checkbox '{textOption}' is not selected, but it should be selected."    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise