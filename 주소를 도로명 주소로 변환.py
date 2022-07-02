from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time




def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
url = 'https://www.juso.go.kr/openIndexPage.do'
driver=set_chrome_driver()
driver.implicitly_wait(3)

driver.get(url)
driver.minimize_window()

search_box = driver.find_element(By.NAME, value="searchKeyword")
for i in range(len(address)):
    search_box.send_keys(address[i])
    search_box.send_keys(Keys.RETURN)
    new_address = str(driver.find_element(By.XPATH,'//*[@id="list1"]/div[1]/span[2]').text)
    new_address_list.append(new_address)
print(new_address_list)
