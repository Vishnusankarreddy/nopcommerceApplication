import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("7032424667")
driver.find_element(By.XPATH, "//input[@id='continue']").click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Vishnu@123")
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("allen solly")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
driver.find_element(By.XPATH, "//li[@id='p_89/Van Heusen']//i[@class='a-icon a-icon-checkbox']").click()
driver.find_element(By.XPATH, "//li[@id='p_n_material_browse/1974776031']//i[@class='a-icon a-icon-checkbox']").click()
driver.find_element(By.XPATH, "//li[@id='p_n_size_browse-vebin/1975396031']//span[@class='a-size-base a-color-base']").click()
time.sleep(60)
driver.quit()
