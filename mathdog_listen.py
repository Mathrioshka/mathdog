import socket
import threading
import os

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

started = False


def restart_software():
    print "Restarting Max/MSP"
    os.system("pskill.exe MaxRT.exe")
    os.system(".\\UDPLife.maxpat")

    global started
    started = False

t = threading.Timer(90, restart_software)


def start_timer():
    global started

    print "Timer started"
    started = True
    reset_timer()


def reset_timer():
    global t

    t.cancel()
    t = threading.Timer(5, restart_software)
    t.start()

while True:
    data, addr = sock.recvfrom(1024)

    if data and not started:
        start_timer()

    reset_timer()
