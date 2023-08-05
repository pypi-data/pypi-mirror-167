import paho.mqtt.client as mqtt
import sys
import os
import subprocess
import base64
import zlib
import sqlite3
import time
from termcolor import colored

from . import config
from . import queries
from . import flake

class Snowbank():
    def __init__(self, filter):
        DB_FILE = str(os.getcwd() + "/" + str(config.initFromConfig('DB_FILE')))
        if DB_FILE is not None:
            self.db_file = DB_FILE
            self.client = mqtt.Client()
            db_conn = sqlite3.connect(self.db_file)
            cursor = db_conn.cursor()
            cursor.execute(queries.create_type_table())
            cursor.execute(queries.create_node_table())
            cursor.execute(queries.create_edge_table())
            cursor.execute(queries.create_graph_table())
            db_conn.commit()
            cursor.close()
        else:
            print("Could not find database file from configuration.")
            sys.exit()
        self.filter = filter

    def generate(self, action):
        db_conn = sqlite3.connect(self.db_file)
        cursor = db_conn.cursor()
        sql = queries.insert_graph(action)
        cursor.execute(sql)
        db_conn.commit()
        cursor.execute(queries.get_last_row_id())
        id = cursor.fetchall()[0][0]
        cursor.close()
        currFlake = flake.FlurryFlake(id, action)
        self.client.user_data_set({'graph': currFlake})
        return currFlake

    def publish(self, msg):
        for topic in self.pub_topics:
            self.client.publish(topic, msg)

    def save(self, graph):
        db_conn = sqlite3.connect(self.db_file)
        save = config.initFromConfig("SAVE_TO_DISK")
        if save == 'yes':
            graph.save_to_disk(db_conn)
        db_conn.commit()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        sub_topics = config.initFromConfig('MQTT_SUBSCRIBE_TOPIC').split()
        for topic in sub_topics:
            client.subscribe(topic, qos=0)
        pub_topics = config.initFromConfig('MQTT_PUBLISH_TOPIC').split()
        self.sub_topics = sub_topics
        self.pub_topics = pub_topics

    def on_message(self, client, userdata, msg):
        decoded_msg = zlib.decompress(base64.b64decode(msg.payload.decode('latin-1'))).decode('latin-1')
        self.filter.load_data(decoded_msg, userdata['graph'])

    def on_disconnect(self, client, userdata, rc=0):
        print("disconnected with result code "+ str(rc))
        self.client.loop_stop()

    def connect_client(self):
        print("Connecting MQTT subscriber...")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        user = config.initFromConfig('MQTT_USERNAME')
        passwd = config.initFromConfig('MQTT_PASSWORD')
        host = config.initFromConfig('MQTT_HOST')
        port = config.initFromConfig('MQTT_PORT')

        self.client.username_pw_set(user, passwd)
        self.client.connect(host, int(port), 60)
        self.client.loop_start()
        time.sleep(1)

    def disconnect_client(self):
        print("Stopping MQTT subscriber...")
        self.client.loop_stop()
