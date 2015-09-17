import os
from time import sleep

from selenium import webdriver

profile_dir = os.path.join(os.environ['HOME'], ".config/google-chrome")
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=%s" % profile_dir)
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(800, 400)
driver.get("chrome://inspect/#devices")
while True:
    inspect = driver.find_element_by_class_name('action')
    if inspect.text == 'inspect':
        break
    sleep(0.5)
inspect.click()
