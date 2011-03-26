from config import Config
import tornado.web
import tornado.ioloop

class Server(object):
	def __init__(self, config=None):
		self.config = config
		if self.config is None:
			self.config = Config()
			self.config.read_all()
	
	def run(self):
		application = tornado.web.Application([
			(r"/(.+)", Handler)
		])
		application.listen(self.config['port'])
		tornado.ioloop.IOLoop.instance().start()

class Handler(object):
	def get(self, path):
		pass
