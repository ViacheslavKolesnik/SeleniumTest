from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.constant.exit_code import ERROR_ELEMENT_PRESENCE_TIMEOUT
from utils.selenium_custom import wait_for_non_empty_text


# class with helpful function to work with selenium
class SeleniumUtils:
	logger = None

	def __init__(self, logger, driver):
		self.logger = logger
		self.driver = driver

	# waits until element is clickable
	# returns element
	def get_clickable_element(self, wait_time, search_rule, search_item):
		try:
			wait = WebDriverWait(self.driver, wait_time)
			element = wait.until(EC.element_to_be_clickable((search_rule, search_item)))

			return element
		except TimeoutException:
			self.logger.exception(f"'{search_item}' clickable wait timeout exceeded.")
			exit(ERROR_ELEMENT_PRESENCE_TIMEOUT)

	# waits until element is present
	# returns element
	def get_element(self, wait_time, search_rule, search_item):
		try:
			wait = WebDriverWait(self.driver, wait_time)
			element = wait.until(EC.presence_of_element_located((search_rule, search_item)))

			return element
		except TimeoutException:
			self.logger.exception(f"'{search_item}' presence wait timeout exceeded.")
			exit(ERROR_ELEMENT_PRESENCE_TIMEOUT)

	# waits until element's text is not empty
	# returns element
	def get_not_empty_text_element(self, wait_time, search_rule, search_item):
		try:
			wait = WebDriverWait(self.driver, wait_time)
			element = wait.until(wait_for_non_empty_text((search_rule, search_item)))

			return element
		except TimeoutException:
			self.logger.exception(f"'{search_item}' presence wait timeout exceeded.")
			exit(ERROR_ELEMENT_PRESENCE_TIMEOUT)

	# waits until all elements are present
	# returns all elements
	def get_all_elements(self, wait_time, search_rule, search_item_rule):
		try:
			wait = WebDriverWait(self.driver, wait_time)
			elements = wait.until(EC.presence_of_all_elements_located((search_rule, search_item_rule)))

			return elements
		except TimeoutException:
			self.logger.exception(f"'{search_item_rule}' presence wait timeout exceeded.")
			exit(ERROR_ELEMENT_PRESENCE_TIMEOUT)
