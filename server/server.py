# -*- coding: utf-8 -*-

import socket
import threading

import json
import logging
import time

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

        # Create logger
        self.logger = logging.getLogger('Tread Socket')
        formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s')
        stream = logging.StreamHandler()
        stream.setLevel(logging.DEBUG)
        stream.setFormatter(formatter)
        self.logger.addHandler(stream)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("[+] New thread socket: %s %s", self.ip, self.port)

    def run(self):

        self.logger.debug("Connexion to %s %s", self.ip, self.port)

        self.clientsocket.settimeout(5)

        a = 0
        while 1:
            try:
                b = "Server's message " + str(a)
                self.clientsocket.send(b)
            except socket.error, exc:
                self.clientsocket.close()
                break
            a = a + 1
            time.sleep(1)

        self.logger.debug("Client disconnect...")

class Server:

    def __init__(self, ip, port, listen):

        self.ip = ip
        self.port = port
        self.listen = listen
        self.active = True

        self.logger = logging.getLogger('server')
        formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s')
        stream = logging.StreamHandler()
        stream.setLevel(logging.DEBUG)
        stream.setFormatter(formatter)
        self.logger.addHandler(stream)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Create socket server - IP : %s - Port : %d - Listen : %d", self.ip, self.port, self.listen)

        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpsock.bind(("", self.port))

    def run(self):

        while self.active:
            self.tcpsock.listen(self.listen)
            self.logger.debug("Listen client...")
            (clientsocket, (self.ip, self.port)) = self.tcpsock.accept()
            newthread = ClientThread(self.ip, self.port, clientsocket)
            newthread.start()

    def stop(self):
        self.active = False
