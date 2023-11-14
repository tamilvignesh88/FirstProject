from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import  time

driver= webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])[1]").click()
driver.find_element(By.XPATH,"(//span[normalize-space()='PIM'])[1]").click()
driver.find_element(By.XPATH,"(//input[@placeholder='Type for hints...'])[1]").send_keys("Logesh raj")
driver.find_element(By.XPATH,"(//button[normalize-space()='Search'])[1]").click()
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.XPATH,"(//button[@type='button'])[6]").click()
driver.find_element(By.XPATH,"(//input)[5]").send_keys("log")
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]").click()
