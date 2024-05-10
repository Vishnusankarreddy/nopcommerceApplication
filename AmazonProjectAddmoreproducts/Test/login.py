from selenium import webdriver

from AmazonProjectAddandDelete.POMProjectdemo.Pages.HomePage import AmazonHomePage, AmazonCartPage
from AmazonProjectAddandDelete.POMProjectdemo.Pages.LoginPage import AmazonSignInPage


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

sign_in_page = AmazonSignInPage(driver)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sign_in_page.enter_email("7032424667")
sign_in_page.click_continue()
sign_in_page.enter_password("Vishnu@123")
sign_in_page.click_sign_in()

home_page = AmazonHomePage(driver)
home_page.search_product("mobile")
home_page.click_first_search_result()
home_page.search_product("pen")
home_page.click_first_search_result()
home_page.search_product("mouse")
home_page.click_first_search_result()

