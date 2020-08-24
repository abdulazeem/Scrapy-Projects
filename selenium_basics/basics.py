from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_path = which('chromedriver')
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://duckduckgo.com/")

search_box = driver.find_element_by_id("search_form_input_homepage")
search_box.send_keys('bikes')
search_box.send_keys(Keys.ENTER)
print(driver.page_source)
driver.close()

# #search_button = driver.find_element_by_id("search_button_homepage")
# search_button.click()
