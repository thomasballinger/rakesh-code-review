def web_server():
  import time, numpy as np
  mysocket = socket.socket()
  mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  try:
    mysocket.bind(('', 1254))
    mysocket.listen(5)

    while True:
      try:
        sockt, stuff = mysocket.accept()
        sockt.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        got_msg = sockt.recv(1000)
        if got_msg.find('GET /favicon.ico') != -1:
          continue
        print stuff, got_msg
        num = np.random.rand()
        msg_send = "My random number: {0}\r\n".format(num)
        print 'Sending {0}'.format(msg_send)
        print sockt.sendall(msg_send)
      finally:
        sockt.close()
  finally:
    mysocket.close()

