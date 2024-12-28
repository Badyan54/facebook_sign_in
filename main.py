from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://www.facebook.com/"
driver = webdriver.Firefox()
driver.get(URL)

email = input("Enter email: ")
passwd = getpass("Enter password: ")
emailInput = driver.find_element(By.ID, "email")
passwdInput = driver.find_element(By.ID, "pass")

emailInput.send_keys(email)
passwdInput.send_keys(passwd)
passwdInput.send_keys(Keys.RETURN)

# driver.close()

