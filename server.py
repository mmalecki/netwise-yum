#! /usr/bin/python

import tornado.ioloop
import tornado.web
import argparse

class MainHandler(tornado.web.RequestHandler):
	def get(self, path):
		print "Request path is: ", self.request.path
		
application = tornado.web.Application([
	(r"/(.+)", MainHandler),
])

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
'''Run netwise-yum server.
netwise-yum is an application which makes sure that you no longer will
have to download the same package more than once, even though using
many computers at once.
It wraps around yum repositories acting like a real server, but caching
all RPMs.
''')
	parser.add_argument('-p', 
	                    help='Port which server will run on.',
	                    type=int,
	                    default=80)             
	args = parser.parse_args()
	
	application.listen(args.p)
	tornado.ioloop.IOLoop.instance().start()
