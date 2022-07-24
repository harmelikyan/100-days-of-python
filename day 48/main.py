from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(price.text)
# Will close the particular tab
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link.text)
# by_xpath = driver.find_element(By.XPATH, '//*[@id="downloads"]/a')
# print(by_xpath.text)
event_date = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')


events = {}

for n in range(len(event_date)):
    events[n] = {
        "time": event_date[n].text,
        "name": event_name[n].text
    }

print(events)

# driver.close()

# Will close the chrome browser
driver.quit()