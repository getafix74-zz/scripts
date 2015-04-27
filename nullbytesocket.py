#!/usr/bin/python

"""
Just another script from the Null Byte tut. This is a simple python socket TCP connection banner grabbing script.

Just add the ip address of the host between the speech marks and fire it up.

It will return the banner of the SSH version.

Steve H 06/04/15
"""

import socket

s=socket.socket()
s.connect(("add ip address here", 22))

answer=s.recv(1024)
print answer

s.close
