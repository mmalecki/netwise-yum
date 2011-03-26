from argparse import ArgumentParser

class Config(object):
	def __init__(self, data={ }):
		self.data = { }
		
	def read_all(self):
		self.read_args()
	
	def __getitem__(self, item):
		return self.data[item]
	
	def read_args(self):
		parser = ArgumentParser(description='Run netwise-yum server.')
		parser.add_argument('-p', 
	                    	help='Port which server will run on.',
	                    	dest='port',
	                    	type=int,
	                    	default=80)             
		args = parser.parse_args().__dict__
		for (k, v) in args.iteritems():
			self.data[k] = v
