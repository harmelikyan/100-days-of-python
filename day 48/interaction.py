from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "anyone can edit")
# all_portals.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

page = driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CLASS_NAME, "btn")
first_name.send_keys("Hungarian")
last_name.send_keys("Fellowship")
email_address.send_keys("email_address@gmail.com")
button.click()

# driver.quit()