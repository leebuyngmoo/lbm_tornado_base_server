#-*- coding: utf-8 -*-
from app import GW_APP
from util import log
import tornado.web, tornado.httpserver
from handlers.tornado_app import tor_app
import os;

from mqtt import mqtt_cli


if __name__=="__main__":
    app = GW_APP('gw_app');

    # 항상 먼저 호출

    #############
    #api server
    port = app.config[app.app_name]["api_port"];
    tor_server_app = tor_app(app);
    http_server = tornado.httpserver.HTTPServer(tor_server_app)
    http_server.listen(port)

    ###############
    # mqtt client #
    ###############
    mqtt = mqtt_cli();
    #################





    try:
        tornado.ioloop.IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit), e:
        tornado.ioloop.IOLoop.instance().stop()


