from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(-1,-1,-1)]
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


"""
To do:
1. Make click faster, but unperfect : https://stackoverflow.com/questions/58048877/increasing-clicking-speed-through-webdriverwait-using-selenium
2. Print (cookies_per_second)
3. Make this bot undetectable: https://stackoverflow.com/questions/58873022/how-can-i-make-a-selenium-script-undetectable-using-geckodriver-and-firefox-thro
4. Show mouse pointer on screen and make it human similar
5. Create User AI Learn mouse moves.
6. Make mouse pointer moves slower, faster, change directions a little bit everytime, like non linear - unperfect.
7. Buying items in the best way (calculate economy model, and make it unperfect sometimes)
8. Exiting small popups on the bottoms sometimes.
9. Saving game sometimes

https://selenium-python.readthedocs.io/waits.html
pyautogui module
https://www.youtube.com/watch?v=OISEEL5eBqg - comments info.
https://en.wikipedia.org/robots.txt
google -> https://www.bing.com/search?form=MOZLBR&pc=MOZD&q=game+bot+selenium+vs
gamebot dinosaur -> https://www.youtube.com/watch?v=XPdWgmS9pjw
X Path -> https://developer.mozilla.org/en-US/docs/Web/XPath
popovers -> https://stacks1.wordpress.com/2017/02/04/how-to-close-popovers-and-in-line-ads-with-selenium-webdriver-2/
ai idea -> https://ai.stackexchange.com/questions/13620/ai-for-selenium-test-automation
make bot GUI by pyQT
"""