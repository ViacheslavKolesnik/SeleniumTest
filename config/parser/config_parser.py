from abc import ABC, abstractmethod


# class for parsing and storing config parameters
# config_file - configuration file
class ConfigurationParser(ABC):
	# initializing method
	# setting configuration file
	@abstractmethod
	def __init__(self, config_file):
		self.number_of_errors_in_configurations = 0
		self.config_file = config_file

	# parse config
	@abstractmethod
	def parse_config(self):
		pass
