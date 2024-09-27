from pywifi import PyWiFi, const, Profile
import time

def scan_wifi():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    time.sleep(1)
    results = ifaces.scan_results()

    for network in results:
        print(f"SSID: {network.ssid}, 信号强度: {network.signal}")

scan_wifi()