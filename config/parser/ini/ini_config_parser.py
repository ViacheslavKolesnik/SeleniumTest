from configparser import ConfigParser

from config.config_parameter.general import GeneralConfig
from config.config_parameter.logger import LoggerConfig
from config.config_parameter.reporter import ReporterConfig
from config.constant.exit_code import *
from config.config import Config
from config.parser.config_parser import ConfigurationParser


# class for parsing and storing config parameters from ini file
# config_file - configuration file
class INIConfigurationParser(ConfigurationParser):
	# initializing method
	def __init__(self, config_file):
		super(INIConfigurationParser, self).__init__(config_file)

	# reading config files into ConfigParser object
	# config_parser - ConfigParser object
	def __read_config_file(self, config_parser):
		try:
			config_parser.read(self.config_file)
			print("Successfully read configuration file.")
		except IOError as e:
			print("IOError occurred while reading config file.")
			exit(EXIT_CODE_FILE_ERROR)
		except:
			print("Error occurred while reading config file.")
			exit(EXIT_CODE_CONFIG_READING_ERROR)

	# reading config file
	# parsing config file
	def parse_config(self):
		config_parser = ConfigParser()

		self.__read_config_file(config_parser)
		self.__parse_config_file(config_parser)

	# parsing config file
	# setting groups of parameters to proper field in Config
	def __parse_config_file(self, config_parser):
		Config.general = self.__parse_general_config(config_parser)
		Config.reporter = self.__parse_reporter_config(config_parser)
		Config.logger = self.__parse_logger_config(config_parser)

		if self.number_of_errors_in_configurations == 0:
			print("Config parsing successful.")
		else:
			print("Config parsing failed. Found {0} errors.".format(self.number_of_errors_in_configurations))
			exit(EXIT_CODE_CONFIG_PARSING_ERROR)

	# parsing general parameters
	# return GeneralConfig object
	def __parse_general_config(self, config_parser):
		initial_general_config = None
		general_config = GeneralConfig()

		try:
			initial_general_config = config_parser['general']
		except Exception:
			print("Error while parsing general configuration occurred.")
			exit(EXIT_CODE_CONFIG_PARSING_ERROR)

		general_config.login = initial_general_config['login']
		general_config.password = initial_general_config['password']

		if initial_general_config['headless'] == 'True':
			general_config.headless = True
		else:
			general_config.headless = False

		if not initial_general_config['element_wait_time'].isdigit():
			self.number_of_errors_in_configurations += 1
			print("element_wait_time must be not negative integer.")
		else:
			general_config.element_wait_time = int(initial_general_config['element_wait_time'])

		return general_config

	# parsing reporter related parameters
	# return ReporterConfig object
	def __parse_reporter_config(self, config_parser):
		initial_reporter_config = None
		reporter_config = ReporterConfig()

		try:
			initial_reporter_config = config_parser['reporter']
		except Exception:
			print("Error while parsing reporter configuration occurred.")
			exit(EXIT_CODE_CONFIG_PARSING_ERROR)

		reporter_config.report_file_path = initial_reporter_config['report_file_path']
		reporter_config.report_file_extension = initial_reporter_config['report_file_extension']

		if initial_reporter_config['console_report'] == 'True':
			reporter_config.console_report = True
		else:
			reporter_config.console_report = False

		if initial_reporter_config['file_report'] == 'True':
			reporter_config.file_report = True
		else:
			reporter_config.file_report = False

		return reporter_config

	# parsing logger related parameters
	# return LoggerConfig object
	def __parse_logger_config(self, config_parser):
		initial_logger_config = None
		logger_config = LoggerConfig()

		try:
			initial_logger_config = config_parser['logger']
		except Exception:
			print("Error while parsing logger configuration occurred.")
			exit(EXIT_CODE_CONFIG_PARSING_ERROR)

		logger_config.log_file_path = initial_logger_config['log_file_path']
		logger_config.log_file_extension = initial_logger_config['log_file_extension']

		if initial_logger_config['console_log'] == 'True':
			logger_config.console_log = True
		else:
			logger_config.console_log = False

		if initial_logger_config['file_log'] == 'True':
			logger_config.file_log = True
		else:
			logger_config.file_log = False

		if not initial_logger_config['log_level'].isdigit():
			self.number_of_errors_in_configurations += 1
			print("log_level must be not negative integer.")
		else:
			logger_config.log_level = int(initial_logger_config['log_level'])

		return logger_config
