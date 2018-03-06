import tornado
import os

from util import log

from handlers.repeathandler import ExampleAPIHandler

from handlers.mqtt_status_handler import MqttAPIHandler
class tor_app(tornado.web.Application):
    ''' Kuo server named Cheese '''
    def __init__(self, hdapp=None):
        self.hdapp = hdapp
        self.config = hdapp.config
        self.template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.config[self.hdapp.app_name]["template_dir"])
        self.static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.config[self.hdapp.app_name]["static_dir"])
        handlers  = [
            (r'/mqtt/(.*)',MqttAPIHandler),

            (r'/test/(.+)',ExampleAPIHandler),
            # (r'/mqtt/',MqttAPIHandler),


            # (r'/excel/(.+)',ExcelAPIHandler),
            # (r'/image/(.+)',fileAPIHandler ),
            # (r'/newestinfo/(.+)',newestAPIHandler ),
            # (r'/newestinfoimage/(.+)',newestInfoFileHandler ),
            # (r'/file/(.+)',fileAPIHandler ),
            # (r'/farminfo/(.+)',FarmInfoAPIHandler ),
            # (r'/excelfileupload/(.+)',ExcelFileUpAPIHandler ),
            # (r'/newest_attrb/(.+)',MongoAPIHandler )
        ]
        settings = dict(debug=self.config[self.hdapp.app_name]['debug'], template_path=self.template_dir, static_path=self.static_dir,
                        cookie_secret=str(self.config[self.hdapp.app_name]['cookie_secret']), login_url='/_signin')
        tornado.web.Application.__init__(self, handlers, **settings)
        log.Wlog('Cheese server is running now  ')
        log.Wlog(self.config[self.hdapp.app_name]['api_port']);

