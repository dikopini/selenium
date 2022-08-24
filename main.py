#belajar selenium

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager as CM


username = 'ngopibareng.ib@gmail.com'
password = 'kopikitasemua'

TIMEOUT = 15

def subs():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    #driver = webdriver.Chrome(executable_path=CM().install(), options=options)
    #driver.set_window_size(600, 1000)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get('https://www.youtube.com/channel/UCeBRbovqggaiv5io94oBhiw')
    time.sleep(2)

    signin_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="end"]/div[2]/ytd-button-renderer')))

    signin_button.click()

    time.sleep(5)

    user_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@class="whsOnd zHQkBf"]')))

    user_element.send_keys(username)

    time.sleep(0.4)

    next_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe '
                      'DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')))

    next_button.click()

    time.sleep(5)


if __name__ == '__main__':
    subs()