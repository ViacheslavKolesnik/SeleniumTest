import logging
import os
from datetime import datetime

from config.constant.exit_code import EXIT_CODE_LOGGER_NOT_SET_UP


# class that handles logger creation and provision
class Logger:
	__logger = None

	# return logger if already setup
	@classmethod
	def get_logger(cls):
		if cls.__logger is None:
			print("Error. You must first setup logger in order to use it.")
			exit(EXIT_CODE_LOGGER_NOT_SET_UP)

		return cls.__logger

	# set up new logger handler
	# create logger if not already created
	@classmethod
	def __setup(cls, handler, log_format):
		if cls.__logger is None:
			cls.__logger = logging.getLogger("SeleniumTest")

		log_formatter = logging.Formatter(log_format)
		handler.setFormatter(log_formatter)
		cls.__logger.addHandler(handler)

	# set up logger
	@classmethod
	def setup(cls, log_format, log_level, console_log, file_log=False, log_file_path=None, log_file_extension=None):
		if console_log:
			handler = logging.StreamHandler()
			cls.__setup(handler, log_format)
		if file_log and log_file_path and log_file_extension:
			os.makedirs(log_file_path, exist_ok=True)
			log_file = log_file_path + str(datetime.now()).replace(':', '-') + log_file_extension
			handler = logging.FileHandler(log_file)
			cls.__setup(handler, log_format)

		cls.__logger.setLevel(log_level)
