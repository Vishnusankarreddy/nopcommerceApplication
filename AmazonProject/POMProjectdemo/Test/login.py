from telnetlib import EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from AmazonProject.POMProjectdemo.Pages.loginPage import AmazonLoginPage, AmazonProductPage

driver = WebDriver()
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

login_page = AmazonLoginPage(driver)
login_page.set_email("7032424667")
login_page.set_continue()
login_page.set_password("Vishnu@123")
login_page.click_sign_in_submit()

product_page = AmazonProductPage(driver)
driver.get("https://www.amazon.com/dp/B07V3MWP4M")
product_page.click_add_to_cart()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "huc-v2-order-row-confirm-text")))

driver.quit()