#!/usr/bin/python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Based on work Copyright (c) 2012 Openstack, LLC.

import Cookie
import os
import socket
import sys
import logging

import websockify

class IwebWebSocketProxy(websockify.WebSocketProxy):
    def __init__(self, *args, **kwargs):
        logging.info('another log...')
        # websockify.WebSocketProxy.__init__(self, unix_target=None, target_cfg=None, ssl_target=None, *args, **kwargs)
        websockify.WebSocketProxy.__init__(self, unix_target=None, ssl_target=None, *args, **kwargs)

    def new_client(self):
        cookie = Cookie.SimpleCookie()
        cookie.load(self.headers.getheader('cookie'))
        token = cookie['token'].value

        from libvirt import openReadOnly
        from xml.etree import ElementTree
        c = openReadOnly(None)
        d = c.lookupByName(token)
        e = ElementTree.fromstring(d.XMLDesc(0))

        host = 'localhost'
        port = int(e.find('.//graphics').get('port'))
        print(port)
        print("alskdjfals")
        tsock = self.socket(host, port, connect=True)

        if self.verbose and not self.daemon:
            print(self.traffic_legend)

        try:
            self.do_proxy(tsock)
        except Exception:
            if tsock:
                tsock.shutdown(socket.SHUT_RDWR)
                tsock.close()
            raise


if __name__ == '__main__':
    logging.info('bla blub')
    print('bla')
    server = IwebWebSocketProxy(listen_host='0.0.0.0', listen_port=5800, source_is_ipv6=False, verbose=True, daemon=False, web='..', target_host='10.0.3.141', target_port='5900', wrap_mode='exit', wrap_cmd=None)
    server.start_server()
print('abababa')
