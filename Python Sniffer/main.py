#!/usr/bin/python

import socket, os, struct, binascii

def analyze_ether_header(data):
    eth_header = struct.unpack("!6s6sH", data[:14]) #IPv4 = 0x0800
    dest_mac = binascii.hexlify(eth_header[0])
    src_mac = binascii.hexlify(eth_header[1])
    proto = eth_header[2]
    print dest_mac
    print src_mac
    print hex(proto)
    data = data[14:]
    return data

def main():
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    recv_data = sniffer_socket.recv(2048)
    analyze_ether_header(recv_data)
    os.system("clear")

while True:
    main()
