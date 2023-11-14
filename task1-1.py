from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import  time

driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])[1]").click()
driver.find_element(By.XPATH,"(//span[normalize-space()='PIM'])[1]").click()
driver.find_element(By.XPATH,"(//button[normalize-space()='Add'])[1]").click()
driver.find_element(By.XPATH,"(//input[@placeholder='First Name'])[1]").send_keys("Logesh")
driver.find_element(By.XPATH,"(//input[@placeholder='Middle Name'])[1]").send_keys("ravi")
driver.find_element(By.XPATH,"(//input[@placeholder='Last Name'])[1]").send_keys("raj")
driver.find_element(By.XPATH,"(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]").click()
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("Loddgje67")
driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys("Test@123")
driver.find_element(By.XPATH,"(//input[@type='password'])[2]").send_keys("Test@123")
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
driver.find_element(By.XPATH,"(//a[normalize-space()='Personal Details'])[1]").click()
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("logu")
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("00S01")
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("driver001")
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[7]").send_keys("nnss001")
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[8]").send_keys("nsis001")
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()

