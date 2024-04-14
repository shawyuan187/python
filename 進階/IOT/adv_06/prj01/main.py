import socket

Host = "localhost"
PORT = 1234
ss = socket.socket()
ss.bind((Host, PORT))
ss.listen(5)

print("IP:{} port:{} start".format(Host, PORT))
client, addr = ss.accept()
print("client address:{},port:{}".format(addr[0], addr[1]))

while True:
    msg = client.recv(128).decode("utf8")
    print("rm:" + msg)
    replly = ""
    if msg == "hi":
        reply = "hi"
        client.send(reply.encode("utf8"))
    elif msg == "bye":
        client.send(b"quit")
        break
    else:
        reply = " ???????????????????????"
        client.send(reply.encode("utf8"))
client.close()
ss.close()
