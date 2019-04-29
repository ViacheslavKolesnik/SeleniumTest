# class for executing operation
class Handler:
	def __init__(self, operation):
		self.__operation = operation

	# execute operation with given arguments
	def handle(self, *args):
		self.__operation(*args)
