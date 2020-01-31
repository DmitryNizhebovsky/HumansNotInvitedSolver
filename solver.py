from selenium import webdriver
import requests
import hashlib
import json
import time
import os

dirname = os.path.dirname(__file__)

URL = 'http://www.humansnotinvited.com/'
ChromeDriverPath = os.path.join(dirname, 'ChromeDriver.exe')
PathToDict = os.path.join(dirname, 'solver_memory.json')
XPathToCategoryName = '/html/body/div/div/div/div/p/strong[1]'

def get_number_matches(category_name, img_hash, memory):
    if category_name in memory:
        if img_hash in memory[category_name]:
            return memory[category_name][img_hash]
        else:
            return 0
    else:
        return 0

with open(PathToDict, 'r') as file:
    memory = json.load(file)

driver = webdriver.Chrome(ChromeDriverPath)
driver.get(URL)

category_name = driver.find_element_by_xpath(XPathToCategoryName).text

images = driver.find_elements_by_class_name('captcha-image')
verify_btn = driver.find_elements_by_class_name('button')[0]
refresh_btn = driver.find_elements_by_class_name('refresh')[0]

for image in images:
    img = image.find_element_by_xpath('./img[1]')
    img_url = img.get_attribute('src')
    img_data = requests.get(img_url).content
    img_hash = str(hashlib.md5(img_data).hexdigest())

    match_number = get_number_matches(category_name, img_hash, memory)

    if match_number > 10:
        image.click()

time.sleep(5)

verify_btn.click()