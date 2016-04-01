import socket
import numpy as np


def web_server():
    mysocket = socket.socket()
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        mysocket.bind(('', 1254))
        mysocket.listen(5)

        while True:
            sockt, address = mysocket.accept()
            try:
                sockt.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                got_msg = ''
                while True:
                    got_msg += sockt.recv(1)
                    if got_msg.endswith('\r\n\r\n') or got_msg.endswith('\n\n'):
                        print 'finished reading request'
                        break
                if got_msg.find('GET /favicon.ico') != -1:
                    continue
                print address, got_msg
                for _ in range(3):
                    num = np.random.rand()
                    msg_send = "My random number: {0}\r\n".format(num)
                    print 'Sending {0}'.format(msg_send)
                    sockt.sendall(msg_send)
            finally:
                sockt.close()
    finally:
        mysocket.close()

web_server()
