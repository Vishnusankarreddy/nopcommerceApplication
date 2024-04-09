from basePackage.BasePo import BasePo


class ElementUtils(BasePo):
    driver = None
    max_retry_attempts = 5

    @staticmethod
    def get_element_by_locator(locator):
        last_exception = None
        page_elements = ElementUtils.driver.find_elements(locator)

    @staticmethod
    def get_text_by_locator(locator):
        element = ElementUtils.get_element_by_locator(locator)
        return element.text