from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from PIL import ImageGrab
from webdriver_manager.chrome import ChromeDriverManager

class Coordinates:
    replay_btn = (340,390)

def restartGame():
    pyautogui.click(Coordinates.replay_btn)

restartGame()


def setup():
    chrome_options = webdriver.ChromeOptions()
    path = "C:/Users/papad/OneDrive/Dokumenty/GitHub/ds_salary_proj/chromedriver.exe"
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    ##Open DinoGame in browser
    driver.get('https://trex-runner.com/')
    return driver


def space(self):
    elem = self.__get_element(self.k, self.v)
    elem.send_keys(Keys.SPACE)



browser = setup()
body = browser.find_element_by_css_selector("body");
body.send_keys(Keys.SPACE);


