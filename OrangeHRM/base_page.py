from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Increased timeout to 20 seconds

    def click(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except TimeoutException:
            print(f"TimeoutException: Could not click on the element with locator {by_locator}")

    def send_keys(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text)
        except TimeoutException:
            print(f"TimeoutException: Could not find the element with locator {by_locator} to send keys")

    def select_by_visible_text(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            select = Select(element)
            select.select_by_visible_text(text)
        except TimeoutException:
            print(f"TimeoutException: Could not find the element with locator {by_locator} to select by visible text")

    def hover_over_element(self, by, value):
        element = self.wait_for_element(by, value)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def click_hr_manager(self):
        self.click(By.XPATH, "//a[text()='IT Manager'][1]")

    def click_book_demo(self):
        self.click(By.XPATH, "//a[contains(text(),'Book a Free Demo')][1]")

    def hover_over_header(self):
        self.hover_over_element(By.XPATH, "//a[text()='Why OrangeHRM']")

    def hover_over_stakeholder(self):
        self.hover_over_element(By.XPATH, "//li[contains(text(),' Stakeholder Solutions')]")