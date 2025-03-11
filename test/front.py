from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://green-frontend-development-dna2g4bqe0fpf6cs.canadacentral-01.azurewebsites.net"
)


try:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    step_1 = driver.find_element(
        By.XPATH, '//*[@id="tabs"]/div[2]/div[1]/div[2]/div/div[1]/h5'
    )
    step_1.click()
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    step_2 = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[1]/a'
    )
    print(step_2.get_attribute("href"))

finally:
    driver.quit()
