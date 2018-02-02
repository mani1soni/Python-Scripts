#!/usr/bin/env python2

import  socket,thread
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#                    ip_type(ipv4) ,  proto_type (UDP)
x.bind(("",9999))
sender_ip="192.168.10.155"
sender_port=8888
#  default ip is binded with port 9999 

def  recv():
	while True:
		data=x.recvfrom(1000)
		print  data[0]


def  send():
	while True:
		rply=raw_input("type here:   ")
		x.sendto(rply,(sender_ip,sender_port))
		

thread.start_new_thread(send,())
thread.start_new_thread(recv,())

while True:
	pass
