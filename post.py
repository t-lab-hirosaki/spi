# -*- coding: utf8 -*-

import socket

HOST        = '192.168.11.80'
PORT        = 51000

def user():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip=s.getsockname()[0]
    s.close()
    return ip

def com_send(mess):
    while True:
        try:
            # 通信の確立
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))

            # メッセージ送信
            user_ip=user()
            mess="ip:" + user_ip + "\nmsg:" + mess
            print(mess)
            sock.send(mess.encode('utf-8'))

            # 通信の終了
            sock.close()
            break

        except:
            print ('retry: ' + mess)
            break

if __name__ == "__main__":
    com_send("hoge")
