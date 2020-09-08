# -*- coding: utf8 -*-

import socket
import sys

HOST        = '192.168.11.80'
PORT        = 51000

if len(sys.argv) != 3:
    print("Error!!")
    print("[Usage:] python3 post.py 学籍番号 message")
    sys.exit()

def user():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip=s.getsockname()[0]
    s.close()
    return ip

def com_send():
    while True:
        try:
            # 通信の確立
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))

            # メッセージ送信
            user_ip=user()
            mess="ip:" + user_ip + "\n" + \
                 "sn:" + sys.argv[1] + "\n" + \
                 "msg:" + sys.argv[2]
            print(mess)
            sock.send(mess.encode('utf-8'))

            # 通信の終了
            sock.close()
            break

        except:
            print('Error!!')
            print('send to failed... ')
            break

if __name__ == "__main__":
    com_send()
