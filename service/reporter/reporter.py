from datetime import datetime

from logger.logger import Logger
from service.file.file_service import FileService
from service.reporter.handler import Handler


# reporter class
class Reporter:
	def __init__(self):
		self.__handlers = list()

	# construct report string
	# friends - list of strings
	# return report string
	def __construct_report(self, friends):
		report = "---------------------------------------\n" \
				 "Report:\n" \
				 "-Friends:\n"
		for link, name in friends.items():
			report += f"--{name}: {link}\n"
		report += "---------------------------------------"

		return report

	# construct report and report to all handlers
	def report(self, friends):
		report = self.__construct_report(friends)
		for handler in self.__handlers:
			handler.handle(report)

	# add console report handler
	def add_console_handler(self):
		console_handler = Handler(print)
		if console_handler not in self.__handlers:
			self.__handlers.append(console_handler)

	# add file report handler
	def add_file_handler(self, file_path, file_extension):
		file_string = file_path + str(datetime.now()).replace(':', '-') + file_extension
		file_service = FileService(Logger.get_logger(), file_string, 'w')
		file_handler = Handler(file_service.write)
		self.__handlers.append(file_handler)

