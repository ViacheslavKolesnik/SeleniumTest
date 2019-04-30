import argparse
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config.config import Config
from config.constant.exit_code import ERROR_CANNOT_NAVIGATE_TO_INVALID_URL
from config.constant.general import *
from config.parser.ini.ini_config_parser import INIConfigurationParser
from logger.logger import Logger
from service.reporter.reporter import Reporter
from utils.selenium import SeleniumUtils


class Launcher:
	# initialization function
	# parse config
	# set up logger
	# create web driver instance
	# return web driver instance
	def __initialize(self):
		config_parser = INIConfigurationParser(DEFAULT_CONFIG)
		self.parse_command_line_arguments(config_parser)
		config_parser.parse_config()

		Logger.setup(LOG_FORMAT,
					 Config.logger.log_level,
					 Config.logger.console_log,
					 Config.logger.file_log,
					 Config.logger.log_file_path,
					 Config.logger.log_file_extension)

		logger = Logger.get_logger()
		logger.info("Logger successfully set up.")

		logger.info("Creating web driver.")
		chrome_options = Options()
		if Config.general.headless:
			chrome_options.add_argument("--headless")
		driver = webdriver.Chrome(chrome_options=chrome_options)

		return driver

	# Parsing command line arguments
	# Set custom config file if given
	def parse_command_line_arguments(self, config_parser):
		argumentParser = argparse.ArgumentParser()

		argumentParser.add_argument('-c', '--config', help='Add custom config file.')

		args = argumentParser.parse_args()

		if args.config:
			config_parser.set_config_file(args.config)

	# log in to facebook
	# return list of user's facebook friends
	def __execute(self, driver):
		logger = Logger.get_logger()
		seleniumUtils = SeleniumUtils(logger, driver)

		logger.info(f"Opening {URL}.")
		try:
			driver.get(URL)
		except WebDriverException:
			logger.exception("Cannot navigate to invalid url.")
			exit(ERROR_CANNOT_NAVIGATE_TO_INVALID_URL)
		driver.maximize_window()

		logger.info("Waiting for email field to be clickable.")
		email_field = seleniumUtils.get_clickable_element(Config.general.element_wait_time, By.ID, ELEMENT_EMAIL_ID)
		logger.info("Writing email.")
		email_field.send_keys(Config.general.login)

		logger.info("Waiting for password field to be clickable.")
		password_field = seleniumUtils.get_clickable_element(Config.general.element_wait_time, By.ID, ELEMENT_PASSWORD_ID)
		logger.info("Writing password.")
		password_field.send_keys(Config.general.password)

		logger.info("Waiting for login button to be clickable.")
		submit_login_button = seleniumUtils.get_clickable_element(Config.general.element_wait_time, By.ID, ELEMENT_LOGIN_BUTTON_ID)
		logger.info("Clicking login button.")
		submit_login_button.click()

		logger.info("Closing popup.")
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

		logger.info("Waiting for profile to be clickable.")
		profile = seleniumUtils.get_clickable_element(Config.general.element_wait_time, By.CSS_SELECTOR, ELEMENT_PROFILE_SELECTOR)
		logger.info("Clicking profile.")
		profile.click()

		logger.info("Waiting for friends tab to be clickable.")
		friends_tab = seleniumUtils.get_clickable_element(Config.general.element_wait_time, By.CSS_SELECTOR, ELEMENT_FRIENDS_TAB_SELECTOR)
		logger.info("Clicking friends tab.")
		friends_tab.click()

		logger.info("Counting friends.")
		friends_count_element = seleniumUtils.get_not_empty_text_element(Config.general.element_wait_time, By.XPATH, ELEMENT_FRIENDS_COUNT_XPATH)
		friends_count = int(friends_count_element.text)

		logger.info(f"You have {friends_count} friends.")

		friends = list()
		if friends_count > 0:
			logger.info("Getting friends names.")
			friends_elements = seleniumUtils.get_all_elements(Config.general.element_wait_time, By.CSS_SELECTOR, ELEMENT_FRIENDS_SELECTOR)
			for friend in friends_elements:
				friends.append(friend.text)

		return friends

	# create reporter
	# report
	def __report(self, friends):
		logger = Logger.get_logger()
		logger.info("Reporting.")
		reporter = Reporter()

		if Config.reporter.console_report:
			reporter.add_console_handler()
		if Config.reporter.file_report:
			reporter.add_file_handler(Config.reporter.report_file_path, Config.reporter.report_file_extension)

		reporter.report(friends)

	# finish program work
	# close web driver
	def __finish(self, driver):
		logger = Logger.get_logger()
		logger.info("Finishing Selenium test.")
		logger.info("Closing driver.")
		driver.close()

	# launch program execution
	def launch(self):
		driver = self.__initialize()
		friends = self.__execute(driver)
		self.__report(friends)
		self.__finish(driver)
