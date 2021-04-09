from appium import webdriver

import time

server = r"http://localhost:4723/wd/hub"

desider = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "automationName": "UiAutomator1",
    "unicodeKeybord":True
}

driver = webdriver.Remote(server,desider)

time.sleep(25)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bfd").click()
driver.swipe(441,1345,452,292)
time.sleep(0.5)

driver.tap([(807,1530)],1)

time.sleep(3)

driver.tap([(754,674)],1)
time.sleep(3)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/l85").click()
time.sleep(20)
driver.tap([(447,1073)],1)
time.sleep(10)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/gsk").send_keys("18787973715")
time.sleep(10)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/ggo").click()
time.sleep(20)
time.sleep(60*5)
driver.quit()