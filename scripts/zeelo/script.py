from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from time import sleep
import os


class zeelo_bot:
  def __init__(self):
    load_dotenv()
    USER_NAME = os.getenv('UNAME')
    PASSWORD = os.getenv('PSWD')
    self.usuario    = USER_NAME
    self.contrasena = PASSWORD
    self.driver     = webdriver.Edge()


  def closeBrowser(self):
    self.driver.close()


  def login(self):
    driver = self.driver
    wait = WebDriverWait(driver, 10)  # A general wait time of 10 seconds

    driver.get("https://app.zeelo.co/my-zeelo")
    #sleep(100000)
    # Wait for the login button to be clickable and then click
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='login_btn']"))).click()
    
    # Input email
    loginUsuario = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='login-email']")))
    loginUsuario.clear()
    loginUsuario.send_keys(self.usuario)

    # Input password and submit
    loginContrasena = driver.find_element(By.XPATH, "//input[@name='password']")
    loginContrasena.clear()
    loginContrasena.send_keys(self.contrasena)
    loginContrasena.send_keys(Keys.RETURN)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='styled__InternalLink-mlmblk-0 cxUVXf styled__ProductTileWrapper-sc-1x8k6ks-1 htEHLG']"))).click() 

    book = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='styled__Clickable-sc-1vvx0m8-7 jiDrwj']")))
    while(len(book) <= 4):
        driver.refresh()
        book = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='styled__Clickable-sc-1vvx0m8-7 jiDrwj']")))
    
    book[2].click()
    
    book = driver.find_elements(By.XPATH, "//p[@class = 'styled__Clickable-sc-1vvx0m8-7 jiDrwj']").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='manage_travel_plans_modal__outbound__select_times_btn']"))).click()
    dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='manage_travel_plans_modal__outbound__time']//div[@class='styled__Container-sc-1u8lcvr-0 KMMSl']//select[@class='styled__Select-sc-1u8lcvr-2 dWThqH']")))
    select = Select(dropdown_element)
    select.select_by_visible_text('06:36')

    # Select from dropdown
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='manage_travel_plans_modal__inbound__select_times_btn']"))).click()
    dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='manage_travel_plans_modal__inbound__time']//div[@class='styled__Container-sc-1u8lcvr-0 KMMSl']//select[@class='styled__Select-sc-1u8lcvr-2 dWThqH']")))
    select = Select(dropdown_element)
    select.select_by_visible_text('17:00')

    # Submit
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='manage_travel_plans_modal__submit_btn']"))).click()

    # Click on dates
    dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='styled__OptionWrapper-uvt67i-2 bIyWqk']")))
    for i in range(0, len(dates)-2):
        date_icon = dates[i].find_element(By.XPATH, "//div[@class='styled__Option-uvt67i-3 gyRYLq']//i[@class='styled__Icon-sc-1c2ayw6-0 bxDTMN material-icons']").click()

    # Confirm
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='manage_travel_plans_modal__replicate__replicate_booking__submit_btn']"))).click()


ig = zeelo_bot()
ig.login()
ig.closeBrowser()
