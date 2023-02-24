# 4. Validate google search functionality

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_01(self):
        filePath = "\Drivers\chromedriver.exe"

        url = "https://www.google.co.in/"

        driver = webdriver.Chrome(filePath)

        time.sleep(1)

        driver.get(url)

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        # Functionality  of search bar
        googleSerach = driver.find_element(By.XPATH, "//input[@title='Search']")
        googleSerach.click()

        if (googleSerach.is_displayed()==True and googleSerach.is_enabled()==True):
            googleSerach.send_keys("python")
            googleSerach.send_keys(Keys.ENTER)
            driver.back()
            time.sleep(1)
        else:
            print("Textbox is not working.")

        time.sleep(1)

        driver.quit()


if __name__ == '__main__':
    unittest.main()
