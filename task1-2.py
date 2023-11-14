from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import  time

driver= webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin12")
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])[1]").click()
