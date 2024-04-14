import socket

cs = socket.socket()
cs.connect(("127.0.0.1", 1234))
while True:
    msg = input("input message")
    cs.send(msg.encode("utf8"))
    reply = cs.recv(128).decode("utf8")
    if reply == "quit":
        print("...")
        cs.close()
        break
    print(reply)
