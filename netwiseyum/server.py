from config import Config
from urlparse import urlparse
import urllib2
import tornado.web
import tornado.ioloop
import os

class Server(object):
    def __init__(self, config=None):
        self.config = config
        if self.config is None:
            self.config = Config()
            self.config.read_all()
	
    def run(self):
        Handler.config = self.config
        application = tornado.web.Application([
            (r"/(.+)", Handler)
        ])
        application.listen(self.config['port'])
        tornado.ioloop.IOLoop.instance().start()

class Handler(tornado.web.RequestHandler):
    config = None
    BLOCK_SIZE = 8192
    
    def __init__(self, *args, **kwargs):
        tornado.web.RequestHandler.__init__(self, *args, **kwargs)
        self.server = urlparse(self.config['server'])
    
    def is_cached(self, filename):
        return os.path.exists(self.make_cache_path(filename))
    
    def make_cache_path(self, filename):
        return os.path.join(self.config['cache'], self.config['server'], filename)
    
    def save_cache(self, filename, content):
        path = self.make_cache_path(filename)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, "w") as f:
            f.write(content)        
        
    def get(self, path):
        print path
        print "Starting download of " + self.config['server'] + '/' + path
        
        resp = urllib2.urlopen(self.config['server'] + '/' + path)
        content = ""
        while True:
            buf = resp.read(self.BLOCK_SIZE)
            if not buf:
                break
            content += buf
            self.write(buf)
        
        print "Downloaded."
        self.save_cache(path, content)
