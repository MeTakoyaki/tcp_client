import socket

target_host="0.0.0.0"
target_port= 9998

#membuat objek soket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#terhubung ke klien
client.connect((target_host,target_port))

#mengirim data
client.send(b"halo igris")

#menerima data
response = client.recv(4096)
print(response.decode())
client.close()