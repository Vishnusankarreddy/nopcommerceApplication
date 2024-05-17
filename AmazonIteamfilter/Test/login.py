import time

from selenium import webdriver

from AmazonIteamfilter.pages.filterpage import AmazonFiltersPage
from AmazonIteamfilter.pages.searchpage import AmazonSearchPage
from AmazonIteamfilter.pages.signpage import AmazonSignInPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# Sign in
sign_in_page = AmazonSignInPage(driver)
sign_in_page.sign_in("7032424667", "Vishnu@123")

# Search for item
search_page = AmazonSearchPage(driver)
search_page.search_for_item("allen solly")

# Apply filters
filters_page = AmazonFiltersPage(driver)
filters_page.apply_filters()

time.sleep(5)
driver.quit()