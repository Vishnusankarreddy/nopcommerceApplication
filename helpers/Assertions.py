import unittest
from helpers.ElementUtils import ElementUtils


class Assertions(ElementUtils):
    @staticmethod
    def  except_to_display(element, error_message):
        Assertions().assertTrue(element.is_displayed(), error_message)

    @staticmethod
    def except_to_display(element, error_message):
        Assertions().assertFalse(element.is_displayed(), error_message)


