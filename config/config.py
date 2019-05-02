# class for storing configs
from config.config_parameter.general import GeneralConfig
from config.config_parameter.logger import LoggerConfig
from config.config_parameter.reporter import ReporterConfig


class Config:
	general = None
	reporter = None
	logger = None

	@classmethod
	def initialize(cls):
		cls.general = GeneralConfig()
		cls.reporter = ReporterConfig()
		cls.logger = LoggerConfig()
