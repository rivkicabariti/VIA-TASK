from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Open_Site():
    global driver
    driver = webdriver.Chrome(executable_path=r"C:/chrome-driver/chromedriver.exe")
    driver.get("https://www.demoblaze.com/")

def Log_In():
    navLinks=driver.find_elements(By.XPATH,'//a[@class="nav-link"]')
    login=[item for item in navLinks  if item.text=="Log in"][0]
    login.click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="loginusername"]').send_keys('Rivka')
    driver.find_element(By.XPATH, '//input[@id="loginpassword"]').send_keys('12345')
    time.sleep(2)
    buttons = driver.find_elements(By.XPATH, '//button[@class="btn btn-primary"]')
    LogInButton = [item for item in buttons if item.text == "Log in"][0]
    LogInButton.click()

def Add_Nexus_6():
    time.sleep(5)
    #check if there is a product with id=3
    try:
        Nexus_6 = driver.find_element(By.XPATH, '//a[contains(@href,"prod.html?idp_=3")]')
    except:
        raise Exception("Product not found")

    time.sleep(5)
    driver.get(Nexus_6.get_attribute('href'))
    time.sleep(5)
    #click on 'Add to Cart' button
    Add_To_Cart = driver.find_elements(By.XPATH, '//a[@class="btn btn-success btn-lg"]')[0]
    time.sleep(2)
    Add_To_Cart.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

def Move_to_cart_section():
    cart = driver.find_elements(By.XPATH, '//a[@id="cartur"]')[0]
    cart.click()

def test_validate():
    time.sleep(5)
    Products_in_cart = driver.find_elements(By.XPATH, '//tr[@class ="success"]')
    time.sleep(5)
    assert len(Products_in_cart)==1, "Sorry, there is more than 1 item in the cart"

    product_details=driver.find_elements(By.XPATH, '//tr[@class ="success"]//td')
    time.sleep(3)
    Price=product_details[2].get_attribute('innerHTML')
    assert Price=="650", "Sorry, the price isn't correct"

    Title=product_details[1].get_attribute('innerHTML')
    assert Title=="Nexus 6", "Sorry, the title isn't correct"


if __name__ == "__main__":
    #a
    Open_Site()
    #b
    Log_In()
    #c
    Add_Nexus_6()
    #d
    Move_to_cart_section()
    #e
    test_validate()