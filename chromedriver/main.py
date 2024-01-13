from selenium import webdriver

""" For pause function"""
import time
from selenium.webdriver.common.by import By



# link
link = "http://localhost/imqa/"


# Defined our Browser
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.XPATH, "//div[@class='loginButton']")
    button.click()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
    print('everything is OK')
