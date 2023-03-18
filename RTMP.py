import sys as A
import uuid as B
import requests as C
import vlc as D
import time as E
from colorama import Fore as F, Style as G, init as H

def I(J):
    K = J.get_state()
    L = str(K).split('.')[1]
    M = E.strftime('%Y-%m-%d %H:%M:%S', E.localtime())
    print(f"{M}: Player status: {L}")

def N():
    H()
    print(F.BLUE + "Cineplex Streaming System Version 3.14 Developed By Lemonito Services" + G.RESET_ALL)
    O = "rtmp://192.168.2.52/Cineplex"
    P = D.Instance()
    J = P.media_player_new()
    Q = P.media_new(O)
    J.set_media(Q)
    J.play()
    E.sleep(1)
    J.set_fullscreen(True)
    I(J)
    try:
        while True:
            E.sleep(60)
            I(J)
    except KeyboardInterrupt:
        J.stop()
        print("Player stopped.")

if __name__ == "__main__":
    R = "https://raw.githubusercontent.com/Thun2552/Cineplex-Stramming-Service/master/Whitelist.txt"
    S = C.get(R)
    T = S.text.splitlines()
    U = str(B.UUID(int=B.getnode()))
    if U in T:
        N()
    else:
        print("Unauthorized hardware.")
        A.exit(1)
