#!/bin/python3
#
# Copyright (c) 2022 北京实耐固连接技术有限公司,Inc.All rights reserved. 
#
# File Name:        mqtt_client.py
# Author:           Liu Fengchen <fengchen.liu@sng.com.cn>
# Created:          2022/9/13 周二
# Description:      包装mqtt的客户端类，开发者可直接调用。、
import socket
from ssl import SSLCertVerificationError

import paho.mqtt.client as mc
import json


class MQTTClient:
    def __init__(self, conf, log):
        self.conf = conf
        self.output_path = conf["output_path"]
        self.log = log
        self.name = conf["client_id"]
        self.client = mc.Client(client_id=self.name)
        self.client.username_pw_set(username=conf["username"], password=conf["password"])
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        if conf["tls_enable"]:
            self.client.tls_set(
                ca_certs=conf["TSL"]["ca_certs"],
                certfile=conf["TSL"]["cert_file"],
                keyfile=conf["TSL"]["key_file"],
                tls_version=mc.ssl.PROTOCOL_TLSv1_2
            )
            self.client.tls_insecure_set(True)

    def connect(self):
        serverstr = str(self.conf['broker']['ip']) + ":" + str(self.conf['broker']['port'])
        try:
            self.client.connect(
                host=self.conf["broker"]["ip"],
                port=self.conf["broker"]["port"]
            )
        except ConnectionError as error:
            self.log.error(f"MQTT连接失败 ({serverstr}): {error.strerror} [Errno:{error.errno}]")
            exit(1)
        except socket.timeout:
            self.log.error(f"MQTT连接超时 ({serverstr})")
            exit(1)
        except SSLCertVerificationError as error:
            self.log.error(f"MQTT证书错误({serverstr}): {error.strerror} [Errno:{error.errno}]")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.log.info(f"{self.name} is connected")
        else:
            self.log.error(f"{self.name} is connection failed")

    def on_message(self, client, userdata, message):
        msg = message.payload.decode("utf-8")
        data = json.loads(msg)
        self.log.debug(f"MQTT Message[{message.topic}]: {msg}")
        if message.topic == "DB/SAVE_ES/TIMER":
            self.weld_data_merger.receive_data(data)
            with open(self.output_path + "hwh_archive.json", "a") as write_f:
                write_f.write(msg)
                write_f.write("\n")
                write_f.close()
        elif message.topic == "DB/SAVE_ES/PLC":
            with open(self.output_path + "plc.json", "a") as write_f:
                print("PLC: ", msg)
                write_f.write(msg)
                write_f.write("\n")
                write_f.close()
        elif message.topic == "DB/SAVE_ES/GUN":
            self.weld_data_merger.receive_data(data)
            with open(self.output_path + "gun.json", "a") as write_f:
                write_f.write(msg)
                write_f.write("\n")
                write_f.close()

    def on_publish(self, client, data, result):
        self.log.info(f"{self.name} mid {result} published data: {data}")

    def on_disconnect(self, client, userdata, rc):
        if rc == 0:
            self.log.warring(f"MQTT已断开连接")
        elif rc == 4:
            self.log.error("MQTT用户名或密码错误")
        elif rc == 5:
            self.log.error("MQTT无权访问")
        elif rc == 7:
            self.log.error("MQTT等待来自服务器的相应超时")
        else:
            self.log.error(f"MQTT意外的断开连接 ({rc})")

    def subscribe(self, topic=None):
        self.client.subscribe(topic)

    def publish(self, msg_dict, topic=None):
        msg = json.dumps(msg_dict)
        ret = self.client.publish(topic, msg)
        return ret

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
