#!/usr/bin/python

import socket
import sys

arg = sys.argv

print "Sweeping doors..."

for port in range(int(arg[2]),int(arg[3])):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)

	if s.connect_ex((sys.argv[1], port)) == 0:
		print "Port",port,"[OPEN]"
		s.close()
