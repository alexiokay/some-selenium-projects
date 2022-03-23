from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/papad/OneDrive/Dokumenty/GitHub/ds_salary_proj/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
link.click()
driver.back()
driver.forward()


try:
    link2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    link2.click()
    driver.back()
    driver.forward()

    link3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link3.click()

    print("page reached")
    time.sleep(2)
    print("going back..")
    driver.back()
    driver.back()
    driver.back()


except:
    print("finish")
