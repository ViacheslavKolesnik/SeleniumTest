import os


# class for working with files
class FileService:
	def __init__(self, logger, file_string, permission):
		self.logger = logger
		self.file_string = file_string
		self.permission = permission

		directory = os.path.dirname(file_string)
		os.makedirs(directory, exist_ok=True)

	# write message to file
	def write(self, message):
		try:
			with open(self.file_string, self.permission) as file:
				file.write(message + '\n')
		except IOError:
			self.logger.exception("IOError occured while writing to file.")
		except Exception:
			self.logger.exception("Error occured while writing to file.")
