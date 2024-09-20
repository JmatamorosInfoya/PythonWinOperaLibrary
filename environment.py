import os
import shutil
import logging
import re
import pyautogui

def before_all(context):
    logging.basicConfig(level=logging.INFO)

def after_step(context, step):
   pass


def after_feature(context, feature):
    print("Test Completed")
    # session = context.config.userdata.get('session')
    # session.findById("wnd[0]/tbar[0]/okcd").text ='/nex'
    # session.findById('wnd[0]').sendVKey(0)
