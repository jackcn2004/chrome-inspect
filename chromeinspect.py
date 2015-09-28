import os
from time import sleep

from selenium import webdriver

def find_ionic_inspect_action(driver):
    browsers = driver.find_elements_by_class_name('browser')
    for browser in browsers:
        name = browser.find_element_by_class_name('browser-name')
        if 'ionic' in name.text:
            action = browser.find_element_by_class_name('action')
            return action
    return None


def wait_for_ionic_inspect_action(driver):
    while True:
        action = find_ionic_inspect_action(driver)
        if action:
            return action
        sleep(0.5)


profile_dir = os.path.join(os.environ['HOME'], ".config/google-chrome")
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=%s" % profile_dir)
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(800, 400)
driver.get("chrome://inspect/#devices")
action = wait_for_ionic_inspect_action(driver)
action.click()
