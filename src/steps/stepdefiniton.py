from behave import given, when, then
from pyjab.jabdriver import JABDriver
import pygetwindow as gw
import re
import win32gui
import os
import time
from selenium import *
import logging
from datetime import datetime
import time
import pyautogui
from dotenv import load_dotenv

load_dotenv()
session = None

logging.basicConfig(
    level=logging.INFO
)

@given('the user launches Opera application')
def step_impl(context):
    time.sleep(5)
    global session
    pattern = r'OPERA(?:(?!Full Service Edition - Version 5\.0\.06\.24\.0 - Internet Explorer).)*?,'
    names = ', '.join(gw.getAllTitles())
    name = ((re.search(pattern, names)).group(0)).rstrip(",")
    
    def get_hwnd_from_title(title):
        hwnd = win32gui.FindWindow(None, title)
        return hwnd
    
    hwnd = get_hwnd_from_title(name)
    path = str(os.getenv('WIN_ACCESS_DRIVER'))
    session = JABDriver(hwnd=hwnd, title=name, bridge_dll=path)
    context.session = session
    return session    

@then('on Opera user clicks on "{x}"')
def step_impl(context, x):
    jabdriver = context.session
    login_btn = jabdriver.find_element_by_name(x)
    login_btn.click()

@then('on Opera user clicks on text that contains "{textOption}"')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"  
    element = jabdriver.find_element_by_xpath(location)
    element.click(simulate=True)

@then('on Opera user selects "{textOption}" from the dropdown')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]]" 
    option = jabdriver.find_element_by_xpath(location)
    option.click()


@then('On opera user clicks on push button "{textOption}"')
def step_impl(context, textOption):
    jabdriver = context.session
    try:
        location_textbox = f"//*[@name=contains('{textOption}')]"
        
        element_textbox = jabdriver.find_element_by_xpath(location_textbox)
        element_info = element_textbox.get_element_information()
        
        push_button_index = element_info.get('index_in_parent') + 1
        
        push_button_element = jabdriver.find_element_by_index_in_parent(push_button_index)
        push_button_info = push_button_element.get_element_information()
        push_button_role = push_button_info.get("role")
        
        if push_button_role == "push button":
            push_button_element.click(simulate=True)
        else:
            raise RuntimeError(f"No push button found adjacent to the textbox with name containing '{textOption}'.")

    except Exception as e:
        raise RuntimeError(f"Failed to perform actions due to: {str(e)}")


@then('on Opera user clicks the push button based on index "{index}"')
def click_specific_push_button(context, index):
    jabdriver = context.session
    try:
        position = int(index)
        element = jabdriver.find_element_by_index_in_parent(position)
        element.click(simulate=True)
    except Exception as e:
        raise RuntimeError(f"Failed to click push button at index {index} due to: {str(e)}")


@then('on Opera user clicks on checkbox "{textOption}"')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"  
    element = jabdriver.find_element_by_xpath(location)
    element.click(simulate=True)
    
    
@then('on Opera user clicks on radio button "{textOption}"')
def step_impl(context, textOption):
    jabdriver = context.session
    location = f"//*[@name=contains('{textOption}')]"  
    element = jabdriver.find_element_by_xpath(location)
    element.click(simulate=True)
    

@then('On opera user get text from textbox with label "{textOption}"')
def step_impl(context, textOption):
    jabdriver = context.session
    try:
        location = f"//*[@name=contains('{textOption}')]"

        element = jabdriver.find_element_by_xpath(location)
        element_info = element.get_element_information()
        textbox_text = element_info.get("text")
        logging.info(f"Textbox text is : {textbox_text}")

    except Exception as e:
        raise RuntimeError(f"Failed to perform actions due to: {str(e)}")
    
@then('on Opera user enter textbox in "{textOption}" with "{inputText}"')
def step_impl(context, textOption, inputText):
    jabdriver = context.session
    try:
        # Locate the element based on its text content
        location = f"//*[@name=contains('{textOption}')]"  
        
        element = jabdriver.find_element_by_xpath(location)
        if element.is_editable():
            element.clear(simulate=True)
            element.send_text(inputText, simulate=True)
        else:
            raise RuntimeError(f"The element containing text '{textOption}' is not editable.")
    except Exception as e:
        raise RuntimeError(f"Failed to fill in '{textOption}' with '{inputText}' due to: {str(e)}")

@then('on Opera user clicks the toolbar button "{textOption}"')
def click_specific_push_button(context, textOption):
    jabdriver = context.session
    try:
        elements = jabdriver.find_elements_by_role("text")        
        for ele in elements:
            ele_info = ele.get_element_information()
            ele_text = ele_info.get("text")
            
            if ele_text == textOption:
                ele.click(simulate=True)
                return
        
        raise RuntimeError(f"Failed to click the button with text '{textOption}'")
    
    except Exception as e:
        raise RuntimeError(f"Failed to click the button with text '{textOption}' due to: {str(e)}")

@then('the opera user waits for "{seconds}" seconds')
def wait_for_seconds(context, seconds):
    jabdriver = context.session
    try:
        seconds = int(seconds)
        time.sleep(seconds)

    except Exception as e:
        raise RuntimeError(f"Error during sleep: {str(e)}")
    

@then('on Opera user presses keyboard key "{action}"')
def step_impl(context, action):
    jabdriver = context.session
    pyautogui.press(action.lower())

@then('on Opera user press keyboard key "{action}" "{times}" times')
def step_impl(context, action,times):
    jabdriver = context.session
    pyautogui.press(action.lower(), presses=int(times))
