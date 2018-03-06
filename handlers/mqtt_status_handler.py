
# -*- coding: utf-8 -*-
'''
Created on 2016. 5. 26.

@author: Sunhong Kim
'''
from handlers import CommonHandler, authenticated_api
import tornado

from mqtt import mqtt_cli

from app import GW_APP

class MqttAPIHandler(CommonHandler):

    @tornado.web.asynchronous
    # @authenticated_api
    @tornado.gen.coroutine
    def get(self,target):
        app = GW_APP();
        result = dict();
        result ["rc"]=1;
        result ["rc_msg"]="ok";
        result["cloud"]=dict();
        result["cloud"]["connect_state"]=mqtt_cli().get_cloud_connect_state();
        result["cloud"]["attempt_state"]=mqtt_cli().get_cloud_connect_attempt_state();
        result["cloud"]["auto_connect"]=app.config[app.app_name]['mqtt']['cloud_mqtt_auto_connect'];

        result["local"]=dict();
        result["local"]["connect_state"]=mqtt_cli().get_local_connect_state();
        result["local"]["attempt_state"]=mqtt_cli().get_local_connect_attempt_state();
        result["local"]["auto_connect"]=app.config[app.app_name]['mqtt']['local_mqtt_auto_connect'];
        self.finish_and_return(result=result)


    @tornado.web.asynchronous
    # @authenticated_api
    @tornado.gen.coroutine
    def post(self,target):
        result=dict();
        # data = self.get_argument('data', True); # get data 받는 방법      ('params name' ,default-data)

        p = self.get_params([
            ('data', True, None),
            ('test', True, None),
        ])





        #
        #
        # if target =='cloud':
        #     print"dd";
        # elif target =='local':
        #     print "dd"
        # else :
        #     print "Dd"






        self.finish_and_return(result={'result': 'example post'})



    @tornado.web.asynchronous
    # @authenticated_api
    @tornado.gen.coroutine
    def delete(self):
        ''' Signout current session (same with GET) '''
        # yield tornado.gen.Task(self.current_session.logout)
        # self.clear_cookie('sid')
        self.finish_and_return(result={'result': 'example post'})