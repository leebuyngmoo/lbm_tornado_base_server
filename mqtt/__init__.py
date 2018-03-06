#-*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
# from Thread.local_mqtt_reconnect import local_mqtt_reconnect
# from Thread.cloud_mqtt_reconnect import cloud_mqtt_reconnect
#
#

from util import log
from util.Singleton import Singleton
from app import GW_APP
class mqtt_cli:
    __metaclass__ = Singleton

    __local_mqtt_connect_state = False;
    __local_mqtt_connect_attempt_state = False;

    __cloud_mqtt_connect_state = False;
    __cloud_mqtt_connect_attempt_state =False;


    def __init__(self):
        log.Ilog("mqtt_cli Singleton __init__");
        self.app= GW_APP();


        ###############
        # auto connect#
        ###############


        self.local_auto_connect = self.app.config[self.app.app_name]['mqtt']['local_mqtt_auto_connect']
        self.cloud_auto_connect = self.app.config[self.app.app_name]['mqtt']['cloud_mqtt_auto_connect']
        if self.local_auto_connect is True: self.do_local_connect();
        if self.cloud_auto_connect is True: self.do_cloud_connect();




    def do_local_connect(self):
        log.Ilog("do_local_connect");
        self.set_local_connect_attempt_state(True);
        self.local_cli = mqtt.Client(self.app.config[self.app.app_name]['mqtt']['local_mqtt_client_id'],True);
        self.local_cli.user_data_set("local")
        self.local_cli.on_connect = self.local_on_connect;
        self.local_cli.on_message = self.local_on_message;
        self.local_cli.on_disconnect = self.local_on_disconnect
        self.local_cli.connect(self.app.config[self.app.app_name]['mqtt']['local_mqtt_host'],self.app.config[self.app.app_name]['mqtt']['local_mqtt_port'],self.app.config[self.app.app_name]['mqtt']['local_mqtt_keepalive'])
        self.local_cli.loop_start()


    def do_local_disconnect(self):
        self.set_local_connect_attempt_state(False);
        self.local_cli.loop_stop();


    def do_cloud_connect(self):
        log.Ilog("do_cloud_connect");
        self.set_cloud_connect_attempt_state(True);
        self.cloud_cli = mqtt.Client(self.app.config[self.app.app_name]['mqtt']['cloud_mqtt_client_id'],True);
        self.cloud_cli.user_data_set("cloud")
        self.cloud_cli.on_connect = self.cloud_on_connect;
        self.cloud_cli.on_message = self.cloud_on_message;
        self.cloud_cli.on_disconnect = self.cloud_on_disconnect
        self.cloud_cli.connect(self.app.config[self.app.app_name]['mqtt']['cloud_mqtt_host'],self.app.config[self.app.app_name]['mqtt']['cloud_mqtt_port'],self.app.config[self.app.app_name]['mqtt']['cloud_mqtt_keepalive'])
        self.cloud_cli.loop_start()

    def do_cloud_disconnect(self):
        self.set_cloud_connect_attempt_state(False);
        self.cloud_cli.loop_stop();






    def local_on_connect(self,client, userdata, flags, rc):
        log.Ilog("local_on_connect");
        self.set_local_connect_state(True);

        # print("Connected with result code "+str(rc))
        # sys_config().local_connected = True;



        # log.Ilog(self,Config().consts['GW']['sensor_will_topic'])
        # log.Ilog(self,Config().consts['GW']['sensor_status_topic'])
        # log.Ilog(self,Config().consts['GW']['sensor_data_topic'])



        # client.publish('/test','asd');
        # client.subscribe('/#');
        # client.subscribe(Config().consts['GW']['sensor_will_topic']);
        # client.subscribe(Config().consts['GW']['sensor_status_topic']);
        # client.subscribe(Config().consts['GW']['sensor_data_topic']);


    def local_on_message(self,client, userdata, msg):
        log.Ilog("local_on_message");

        # topic = str(msg.topic).split('/');
        #
        # stre = str(msg.topic)+"               "+str(msg.payload);
        #
        #
        # # 내상테 가 active 상태일때  heatbeat  topic 은 내가 보내는것이기때문에    내가 active 상태 일때는 heartbeat 무시
        #
        #
        #
        # Log().log(self,stre)

    def local_on_disconnect(self, _, __, ___):
        log.Ilog("local_on_disconnect");
        self.set_local_connect_state(False);














    def cloud_on_connect(self,client, userdata, flags, rc):
        log.Ilog("cloud_on_connect")
        self.set_cloud_connect_state(True)


    def cloud_on_message(self,client, userdata, msg):
        log.Ilog("cloud_on_message")

        topic = str(msg.topic).split('/');

        stre = str(msg.topic)+"               "+str(msg.payload);


        # Log().log(self,stre)

    def cloud_on_disconnect(self, _, __, ___):
        log.Ilog("cloud_on_disconnect")
        self.set_cloud_connect_state(False)

        # sys_config().cloud_connected = False;
















###################
    #getter setter
######################

    def get_local_connect_state(self):
        # log.Ilog("get_local_connect_state")

        return self.__local_mqtt_connect_state;

    def get_cloud_connect_state(self):
        # log.Ilog("get_cloud_connect_state")

        return self.__cloud_mqtt_connect_state;

    def set_local_connect_state(self,state):
        log.Ilog("set_local_connect_state")
        self.__local_mqtt_connect_state =state;

    def set_cloud_connect_state(self,state):
        log.Ilog("set_cloud_connect_state")
        self.__cloud_mqtt_connect_state=state

    def get_local_connect_attempt_state(self):
        return self.__local_mqtt_connect_attempt_state;

    def get_cloud_connect_attempt_state(self):
        return self.__cloud_mqtt_connect_attempt_state;

    def set_local_connect_attempt_state(self,state):
        self.__local_mqtt_connect_attempt_state =state;

    def set_cloud_connect_attempt_state(self,state):
        self.__cloud_mqtt_connect_attempt_state=state;





